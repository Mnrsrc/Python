# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:54:19 2019

@author: Munire
"""
import numpy as np
array1=np.array([52, 24, 14, 13])
array2=np.arange(42,46)
decraceOfArrays=array1-array2
print(decraceOfArrays)

squareOfArrray2=array2**2
print(squareOfArrray2)
CubeOfArray1=array1**3
print(CubeOfArray1)
#USAGE 1
matrix1=np.array([[0,0],[0,0]])
matrix2=np.array([[0,0],[0,0]])
crossedMatrixs=matrix1*matrix2
print("Crossed Matrixs: \n" + str(crossedMatrixs))
#USAGE 2
matrix3=np.array([[5,4,7],[4,6,2]])
matrix4=np.array([[7,8],[2,5],[0,0]])
crossedMatrixs2=matrix3@matrix4
print("Crossed Matrix2: \n" + str(crossedMatrixs2))
#USAGE 3
crossedMatrixs3=matrix3.dot(matrix4)
print("Crossed Matrix3: \n" + str(crossedMatrixs3))
#%%TRIGONOMETRİC FUNCTIONS???????
sinusValue=np.sin(90)
print(sinusValue)

print(array1>20)

crossedArrays=array1*array2
print(crossedArrays)

#%%ALLOCATION 0,1
zeroMatrix=np.zeros((5,4))
oneMatrix=np.ones((2,3))
print("Zero and One Matrixs: \n" + str(zeroMatrix) + " \n****\n" + str(oneMatrix))

#%%RANDOM ---->???How many number generate ??????
randomNumberGenerator=np.random.random((2,4))
print("Random Number: " +str(randomNumberGenerator))

#%% FOUR TRANSACTIONS and OTHER TRANSACTIONS:
sumMatrix=matrix3.sum()
print("Sum of Matrix3: " + str(sumMatrix))
minMatrix=matrix1.min()
maxMatrix=np.max(matrix3)
print("Minimum number of  in the Matrix1: " +str(minMatrix)+ "\nMaximum number of in the Matrix3: " + str(maxMatrix))
squareRootMatrix=np.sqrt(matrix4)
print("Square root of Matrix4: " + str(squareRootMatrix))


















