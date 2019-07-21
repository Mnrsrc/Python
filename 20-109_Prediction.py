# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:31:58 2019

@author: Munire
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data=pd.read_csv("hw_25000.csv")
regression=LinearRegression()
height=data.Height.values.reshape(-1,1)
weight=data.Weight.values.reshape(-1,1)
regression.fit(height,weight)
#IT DOESN'T WORK!!!!!!!!!!!
#print(regression.predict(71))

plt.scatter(data.Height,data.Weight)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

