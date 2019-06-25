# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:33:33 2019

@author: Munire
"""
import numpy as np
#What is 50 or 4 or another numbers means?
number1=np.floor(50*np.random.random((3,4)))
print(number1)
print(number1.shape)
print(number1.reshape(12,1))
#ERROR!!!
#print(number1.reshape(5,2))

print("Transpoze of that  is named number1: \n" + str(number1.T))
print("Resshape of number1 with 6 rows and another values is random arranged:  "+str(number1.reshape(6,-1)))
#ERROR
#print("Reshape: " + str(number1.reshape(5,-1)))