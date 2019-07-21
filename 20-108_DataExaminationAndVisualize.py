# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 09:51:25 2019

@author: Munire
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('hw_25000.csv')
plt.scatter(data.Height,data.Weight)
#plt.show()
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
