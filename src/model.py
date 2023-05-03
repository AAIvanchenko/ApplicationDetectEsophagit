from ultralytics import YOLO
from torch import load
import torch.nn as nn

PATH_WEIGHT_DETECTION = "E:/7/KPP/ApplicationDetectEsophagit/weights_model/detection/best_yolov8.pt"
PATH_WEIGHT_CLASSIFICATION = "E:/7/KPP/ApplicationDetectEsophagit/weights_model/classification/densnet121_softmax_eph50.pt"

class ModelDetect(nn.Module):
    def __init__(self):
        super(ModelDetect, self).__init__()
        self.model = YOLO(PATH_WEIGHT_DETECTION)
        self.model.val()

    def forward(self, img, conf=0.8):
        # картику не нужно преобразовывать в torch после прочтения cv2
        predict = self.model.predict(source=img, conf=conf)
        return predict


class ModelClassificationZLine(nn.Module):
    def __init__(self):
        super(ModelClassificationZLine, self).__init__()
        self.model = load(PATH_WEIGHT_CLASSIFICATION)
    
    def forward(self, img):
        # картинка прочитана и переведена в торч
        predict = self.model(img)
        return predict
    


    
