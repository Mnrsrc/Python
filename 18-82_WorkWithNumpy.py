# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:39:57 2019

@author: Munire
"""
import numpy as np
numbers=np.arange(2,10)
print(numbers)
print("Type of numbers: " + str(numbers.dtype))

myNumberArray=np.array([1,4,7,10,13,16,19,22,25,28,31,33])
print(myNumberArray)
print("Type of my arrays: " + str(myNumberArray.dtype))

myNumberArray2=np.array([1,4,7,10,13,16,19,22,25,28,31,34.65])
print(myNumberArray2)
print("Type of my arrays: " + str(myNumberArray2.dtype))

myNumberArray3=np.array([1,4,7,10,13,16,19,22,25,28,31,31.54,"Münire"])
print(myNumberArray3)
print("Type of my arrays: " + str(myNumberArray3.dtype))

myArray=np.array([[12,5],[54,54],[52,2],[1,0]])
print(myArray)
print("Type of: " + str(myArray.dtype) + "\t" + "and Size of: " + str(myArray.ndim))
print("Item number of my array: " + str(myNumberArray.size))
print("My array of Reshape that 3*2 matrix: \n" + str(myNumberArray.reshape(6,2)))
print("*******")
#OTHER USAGE:
a=myNumberArray.reshape(4,3)
print(a)