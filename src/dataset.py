from pathlib import Path
import cv2
import numpy as np

VID_FORMATS = ['mp4', 'mkv']

class VideoToBatchImage:
    def __init__(self, path, img_size=640, scaleFill=False, padding=None, stride=None, transforms = None):
        p = Path(path).resolve()

        if p.is_file():
            if p.suffix[1:].lower() in VID_FORMATS:
                path_video = str(p)  # files
        else:
            raise FileNotFoundError(f'{p} does not exist')
        
        # проверку перенести сюда
        img_info = self.get_video_info(path_video)
        # Расчёт stride для каждого видео
        vid_stride = int(img_info["fps"]*stride) if stride else 1
        vid_stride_frames = vid_stride
        
        # Проверка на количество кадров
        self.num_frames = img_info["frames"]
    
        if isinstance(img_size, int):
            img_size = (img_size, img_size)
        
        self.transforms = transforms
        self.path = path_video
        self.img_size = img_size
        self.vid_stride_frames = vid_stride_frames
        self.padding = padding
        self.scaleFill = scaleFill
        
    def __iter__(self):
        self.new_video(self.path)
        return self
    
    def __next__(self):
        if self.cap == None:
            raise StopIteration
        path = self.path

        # Read video
        # print('start', self.cap.get(cv2.CAP_PROP_POS_MSEC)/1000, self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        ret_val, img0 = self.cap.read()
        assert ret_val is True, f'Error to read from file on {round(int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))/self.cap.get(cv2.CAP_PROP_FPS), 2)} sec by path:{path}'
        self.frame += 1

        # Skip Frames
        self.frame += self.vid_stride_frames - 1

        if self.frame >= self.num_frames:
            self.cap.release()
            self.cap = None
        # print(self.frame)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame)
        # print('count_frame', int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)))

        img = letterbox(img0, self.img_size, scaleFill=self.scaleFill)
        # Convert
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR to RGB
        
        if self.transforms:
            img = self.transforms(img)

        return img
    
    def get_video_info(self, path):
        cap = cv2.VideoCapture(path)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        res_info = {}
        res_info["frames"] = length
        res_info["fps"] = fps
        cap.release()
        return res_info
    
    def new_video(self, path):
        self.frame = 0
        self.cap = cv2.VideoCapture(path)
        self.frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if self.padding:
            self.frame += self.padding
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.padding)
    
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