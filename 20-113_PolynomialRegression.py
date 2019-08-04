# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:38:11 2019

@author: Munire
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
 
data=pd.read_csv("positions.csv")
data.columns=["position","level","salary"]

level=data.iloc[:,1].values.reshape(-1,1)
salary=data.iloc[:,2].values.reshape(-1,1)
regressionPoly=PolynomialFeatures(degree=4)
levelPoly=regressionPoly.fit_transform(level)

regression=LinearRegression()
regression.fit(level,salary)
plt.xlabel("Level")
plt.ylabel("Salary")
plt.scatter(level,salary)

x=np.arange(min(level),max(level)).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red")
#plt.annotate("Linear",xy=(2,2500),xytext=(6,3000),arrowprops=dict(facecolor='black', shrink=0.05),
#            horizontalalignment='right',
#            verticalalignment='bottom',)
regression2=LinearRegression()
regression2.fit(levelPoly,salary)
prediction=regression.predict([[8.3]])
prediction2=regression2.predict(regressionPoly.fit_transform(np.array([[5.2]])))
print("Prediction is for level 5.2 with Linear Regression:"+ str(prediction))
print("Prediction is for level 5.2 with Polynomial Regression:" + str(prediction2))
plt.plot(level,regression2.predict(levelPoly))
plt.show()