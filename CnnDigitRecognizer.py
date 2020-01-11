# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:46:13 2019

@author: Munire
"""

#import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



#load dataset
#dataset overview
#Now  we have 2 numpy files X.npy and Y.npy. So we need to load them.

dataset1=np.load('X.npy')
print(dataset1)

dataset2=np.load('Y.npy')
print(dataset2)
#Determine to variables
imageSize=64
#We can shown as in the figure.For example we want to see what is in the 12. data. 
#If you run it, you can see "3" digit data with the fingers of hand in the 12. data.
plt.imshow(dataset1[12].reshape(imageSize,imageSize))
#Now, we do not want to see the with axises.(Optional)
plt.axis("off")

#training and testing data

#Normalizationing Data
#Reshape Data
#Label Encoding
#Train and Test Split
#CNN-Same Padding
#CNN-Max Pooling
#Flattening
#Full Connection
#Create Model
#Define Optimizer
#Compile Model
#Epochs and Batch Size
#Data Augmentation
#Fit the Model
#Evaluate the Model