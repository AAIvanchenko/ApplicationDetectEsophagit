from src.predict import PredictClassification, PredictDetection

PATH_SAVE = 'prediction'

class StartPredict():
    def __init__(self, path_video):
        self.pred_classification = PredictClassification(path_video=path_video)

        if  len(self.pred_classification) > 0:
            PredictDetection(PATH_SAVE, self.pred_classification)

