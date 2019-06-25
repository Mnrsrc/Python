# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:34:06 2019

@author: Munire
"""
import numpy as np
dataset=[14,15,171,25,8,98,75,54,25]

print(np.arange(15).reshape(3,5))
numpyData=np.arange(14)
print(type(numpyData))

numpyData2=np.arange(215)
print(numpyData2.shape)
#%% 
numpyData3=np.arange(15).reshape(3,5,1,1)
print("Size of: " + str(numpyData3.ndim))
