
from url_processor import process_url
import tensorflow as tf
import numpy as np
model = tf.keras.models.load_model('models/model14.keras')



def predict_url(features):
    if features is None:
        return "Invalid Domain"
    prediction = model.predict(features)
    threshold = 0.5
    binary_predictions = [1 if pred >= threshold else 0 for pred in prediction]
    if 0 in binary_predictions:
        result = 'Legitimate'
    elif 1 in binary_predictions:
        result = 'Phishing'
    return result

