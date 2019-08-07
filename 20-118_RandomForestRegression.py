# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:55:18 2019

@author: Munire
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data=pd.read_csv("positions.csv")
level=data.Level.values.reshape(-1,1)
salary=data.Salary.values
#For Different Results
regression=RandomForestRegressor(n_estimators=5)
regression.fit(level,salary)
prediction=regression.predict(np.array([[1.4],[3.4],[5.4],[7.4],[9.4]]))
print("Different results  for some data in each cycle:" + str(prediction))
regression2=RandomForestRegressor(n_estimators=10, random_state=2)
regression2.fit(level,salary)
prediction2=regression2.predict(np.array([[1.4],[2.4],[3.4],[4.4],[5.4],[6.4],[7.4],[8.4],[9.4]]))
print("Same results for some data in each cycle:" + str(prediction2))
plt.scatter(level,salary)
plt.show()