from ultralytics import YOLO
from torch import load
import torch

PATH_WEIGHT_DETECTION = "E:/7/KPP/ApplicationDetectEsophagit/weights_model/detection/best_yolov8.pt"
PATH_WEIGHT_CLASSIFICATION = "E:/7/KPP/ApplicationDetectEsophagit/weights_model/classification/densnet121_softmax_eph50.pt"

class ModelDetect(torch.nn.Module):
    def __init__(self):
        super(ModelDetect, self).__init__()
        self.model = YOLO(PATH_WEIGHT_DETECTION)
        self.model.val()

    def forward(self, img, conf=0.8):
        # картику не нужно преобразовывать в torch после прочтения cv2
        predict = self.model.predict(source=img, conf=conf)
        return predict


class ModelClassificationZLine(torch.nn.Module):
    def __init__(self):
        super(ModelClassificationZLine, self).__init__()
        self.model = torch.load(PATH_WEIGHT_CLASSIFICATION)
        self.device = torch.device("cuda") if torch.cuda.is_available else torch.device("cpu")
    
    def img_to_tensor(self, img):
        img = img.copy()
        img = img.transpose((2, 0, 1))
        img = torch.from_numpy(img).to(torch.float32)
        img /= 255  # 0 - 255 to 0.0 - 1.0
        if len(img.shape) == 3:
            img = img.unsqueeze(0)
        return img
    
    def forward(self, img):
        img = self.img_to_tensor(img).to(self.device)
        predict = self.model(img).to(self.device)
        return predict
    