import sys
import feature_extractor as fex
import pandas as pd
import joblib
import tensorflow as tf

tf.config.set_visible_devices([], 'GPU')


def process_url(url_input):
    #Extract features of url
    features = fex.extract_features(url_input) #returns dictionary 
    
    if features == None:
        return None
    
    #Convert dictionary to pandas dataframe
    features_df = pd.DataFrame([features])
    
    #Fit MinMaxScaler to training data
    scaler = joblib.load('models/scaler.save')
    
    #Transform extracted features using scaler
    features_df_scaled = scaler.transform(features_df)
    
    return features_df_scaled

