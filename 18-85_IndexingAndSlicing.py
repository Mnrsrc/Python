# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:28:14 2019

@author: Munire
"""
import numpy as np
numbers=np.array([0.4,14,10,5,47])
#print(numbers[6]) //INCORRECT
print("First Number in the numpy array: "+str(numbers[0]))
numbers2=np.array([[24,1,0,5],[52,14,10,1]])
print("First Row in matrix: "+str(numbers2[0]))
print("Second value in the first row of matrix: " +str(numbers2[1][2]))
#OTHER USAGE
print("Second value in the first row of matrix: " +str(numbers2[1,2]))
print("All rows' value in the third columns of matrix: "+str(numbers2[:,3]))
print("All columns' value in the between  from 1 to 3 rows:  "+str(numbers2[1:3,:]))
print("Reverse order of single matrix: "+str(numbers[::-1]))
print("Values in the last row: " + str(numbers2[-1,:]))
print("Values in the last columns: " + str(numbers2[:,-1]))