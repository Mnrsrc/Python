# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:44:17 2019

@author: Munire
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
data=pd.read_csv('hw_25000.csv')
plt.xlabel("Height")
plt.ylabel('Weight')

height=data.Height.values.reshape(-1,1)
weight=data.Weight.values.reshape(-1,1)

regression=LinearRegression()
regression.fit(height,weight)
plt.scatter(data.Height,data.Weight)
x=np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red")
plt.title("Simple Linear Regression Model")
print(r2_score(weight,regression.predict(height)))
plt.show()
