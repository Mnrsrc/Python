# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:43:15 2019

@author: Munire
"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot  as plt

data=pd.read_csv("positions.csv")
level=data.iloc[:,1].values.reshape(-1,1)
salary=data.iloc[:,2].values.reshape(-1,1)

regression=DecisionTreeRegressor()
regression.fit(level,salary)
predict=regression.predict(np.array([[7.4]]))
print("Salary prediction for level 7.4: " + str(predict))
x=np.arange(min(level),max(level),0.05).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Decision Tree Regressor")


plt.scatter(level,salary)
plt.show()
