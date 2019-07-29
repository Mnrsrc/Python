# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:15:07 2019

@author: Munire
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data=pd.read_csv('insurance.csv')
print(data.columns)
ageBmi=data.iloc[:,[0,2]].values

expenses=data.expenses.values.reshape(-1,1)

regression=LinearRegression()
regression.fit(ageBmi,expenses)
predict=regression.predict(np.array([[20,20]]))
print("Expenses prediction of 20 years old and 20 bmi person:" + str(predict))
print("Spending distrubtions according to same age but different bmi"+ str(regression.predict(np.array([[30,16],[30,21],[30,26],[30,31],[30,36],[30,41],[30,46],[30,51],[30,53]]))))
