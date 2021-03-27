import joblib
import os
import pandas as pd

class PricePredictor:

    def __init__(self):
        currentFolderName = os.path.dirname(os.path.abspath(__file__))
        randomForestModelPath = os.path.join(currentFolderName, 'random_forest.model')
        with open(randomForestModelPath, 'rb') as model:
            self.model = joblib.load(model)

    def predict(self, request):
        predictionInput = pd.DataFrame(request)
        return self.model.predict(predictionInput)