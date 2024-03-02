
from url_processor import process_url
import joblib
import numpy as np
model = joblib.load('models/fmodel1.save')



def predict_url(features):
    prediction = model.predict(features)
    threshold = 0.5
    binary_predictions = [1 if pred >= threshold else 0 for pred in prediction]
    binary_predictions = np.where(prediction >= threshold, 1, 0)
    return binary_predictions.tolist()