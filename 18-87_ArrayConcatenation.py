# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:48:35 2019

@author: Munire
"""
import numpy as np

array1=np.floor(20*np.random.random((5,2)))
print("Flatted version of array1 \n: " +str(array1))
array2=np.floor(2*np.random.random((3,2)))
print("Flatted version of array1 \n: " + str(array2))
array3=np.floor(5*np.random.random((5,8)))
print("Flatted version of array3: \n" + str(array3))
print("Stacked version in same vertical: \n " + str(np.vstack((array1,array2))))
print("Stacked version in same horizontal: \n" + str(np.hstack((array1,array3))))