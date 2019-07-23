# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:13:13 2019

@author: Munire
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
data=pd.read_csv('hw_25000.csv')
plt.xlabel('Height')
plt.ylabel('Weight')
height=data.Height.values.reshape(-1,1)
weight=data.Weight.values.reshape(-1,1)


regression=LinearRegression()
regression.fit(height,weight)
plt.scatter(data.Height,data.Weight)
#It does not work!!!
#result=regression.predict(71)
#print("****")
#print(result)
x=np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red")
plt.title("Linear Regression Model:")
plt.show()