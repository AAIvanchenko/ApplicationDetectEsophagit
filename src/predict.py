import torch

from dataset import VideoToBatchImage
from model import ModelClassificationZLine

TRESHOLD_ZLINE = 25
TRESHOLD_NOTLINE = 80 
TRESHOLD_COUNT_TRUE_PRED = 3
TRESHOLD_COUNT_FALSE_PRED = 5

class PredictClassification():
    def __init__(self, path_video):
        self.model = ModelClassificationZLine()
        self.dataset = VideoToBatchImage(path_video)
        
        self.count_true = 0
        self.count_false = 0
        self.list_img_true = []
        self.list_img_false = []
        self.res = []

        for img in self.dataset:
            self.check_classification(img, self.predict(img))
    
    def predict(self, img):
        pred = self.model(img)

        return pred
    
    def check_classification(self, img, predict):
        """
        Метод работает над проверкой изображений, выделяет те, изображения,
        на которых есть z-линия.

        img: текущее изображение
        predict: предсказание классификатора на изобр.

        return: список картинок, которые можно подавать детектору.
        """
        fanc_pred_proc = lambda x: round(x.item() * 100, 4)
        pred_zline = fanc_pred_proc(predict[0][1])
        pred_notline = fanc_pred_proc(predict[0][0])
        
        if pred_zline > TRESHOLD_ZLINE and self.count_true < TRESHOLD_COUNT_TRUE_PRED:
            self.count_false = 0
            self.count_true += 1
            self.list_img_true.append(img)
        elif pred_notline >= TRESHOLD_NOTLINE:
            self.count_true = 0
            self.list_img_false.append(img)
            self.count_false += 1

        if self.count_false > TRESHOLD_COUNT_FALSE_PRED:
            self.list_img_true = []
            self.list_img_false = []
        if self.count_true > TRESHOLD_COUNT_TRUE_PRED:
            if len(self.list_img_false) > 0:
                self.res = self.list_img_true + self.list_img_false
            else:
                self.res = self.list_img_true

            self.list_img_true = []
            self.list_img_false = []
            
        return self.res

    def save_res(self):
        """
        Метод для сохранения изображений в директорию проекта.
        """
        pass
