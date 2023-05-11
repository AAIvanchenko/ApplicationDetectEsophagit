import os
from src.predict import PredictClassification, PredictDetection

PATH_SAVE = '../prediction'

class StartPredict():
    def __init__(self, path_video) -> None:
        self.pred_classification = PredictClassification(path_video=path_video)

        if  len(self.pred_classification) <= 0:
            return 'Не было найдено z-линии желудка'
        else:
            self.pred_detection = PredictDetection(PATH_SAVE, self.pred_classification)
            # прошла детекция
            if len(os.listdir(PATH_SAVE)) == 0:
                return 'Не было обноружено болезни'
            else:
                return ''
