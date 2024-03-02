#!/usr/bin/env python3
# coding: utf-8

# In[1]:


import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn import preprocessing
import statistics


# In[2]:


import tensorflow as tf


# In[3]:


tf.config.set_visible_devices([], 'GPU')


# In[4]:


df = pd.read_csv('Data/dataset_phishing.csv')


# In[5]:


df.head()


# In[6]:


#split dataset into features (X) and target variables (y)
X = df.drop(columns = ['url','status','domain_in_brand', 'brand_in_subdomain', 'brand_in_path', 'random_domain'])
y = df['status']


# In[7]:


column_ranges = X.max() - X.min()


# In[8]:


features_to_drop = column_ranges[column_ranges == 0].index


# In[9]:


features_to_drop


# In[10]:


X = X.drop(features_to_drop, axis=1)


# In[11]:


#create train and test sets
#stratify to ensure proportional split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15, stratify=y)


# In[12]:


label_encoder = preprocessing.LabelEncoder()


# In[13]:


y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)


# In[14]:


#fit scaler on training data
scaler = preprocessing.MinMaxScaler()


# In[15]:


X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[16]:


#Find shape of data to specify input shape when building CNN
data_shape = X_train_scaled.shape
print("Data shape:", data_shape)


# In[17]:


data_shape = X_train_scaled.shape
print("Data shape:", data_shape)

