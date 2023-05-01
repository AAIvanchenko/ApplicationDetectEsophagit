import cv2
import numpy as np

def letterbox(im, new_shape=(640, 640), color=(0, 0, 0), scaleFill=False, scaleup=False):
    # Resize and pad image while meeting stride-multiple constraints
    shape = im.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:  # only scale down, do not scale up (for better val mAP)
        r = min(r, 1.0)

    # Compute padding
    # ratio = r, r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    if scaleFill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        # ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return im

def find_mask(img):
    """
    Удаление черных границ по маске.
    """
    # Convert Image to Image HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Defining lower and upper bound HSV values
    lower = np.array([0,0,0])
    upper = np.array([350,20,90])

    # Defining mask for detecting color
    mask = cv2.inRange(hsv, lower, upper)

    # invert mask
    mask = cv2.bitwise_not(mask)
    
    return mask

def del_area_behind_countour(img):
    mask_img = find_mask(img)
    mask_img = cv2.GaussianBlur(mask_img, (11,11), 10)

    _, thresh = cv2.threshold(mask_img, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    mask = np.zeros(img.shape[0:2], dtype=np.uint8)

    points = sorted(contours, key= lambda c: len(c))[-1]

    #method 1 smooth region
    cv2.drawContours(mask, [points], -1, (255, 255, 255), -1, cv2.LINE_AA)
    res = cv2.bitwise_and(img, img, mask = mask)
    rect = cv2.boundingRect(points) # returns (x,y,w,h) of the rect
    img_cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
    
    return img_cropped

