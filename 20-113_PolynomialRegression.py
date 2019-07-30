# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:38:11 2019

@author: Munire
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
 
data=pd.read_csv("positions.csv")
data.columns=["position","level","salary"]

level=data.iloc[:,1].values.reshape(-1,1)
salary=data.iloc[:,2].values.reshape(-1,1)
regression=LinearRegression()
regression.fit(level,salary)
plt.xlabel("Level")
plt.ylabel("Salary")
plt.scatter(level,salary)
x=np.arange(min(level),max(level)).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red")
tahmin=regression.predict([[8.3]])
print("Prediction is for level-5:"+ str(tahmin))
plt.show()