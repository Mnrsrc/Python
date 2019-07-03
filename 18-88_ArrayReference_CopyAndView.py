# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:13:04 2019

@author: Munire
"""
import numpy as np
array1=np.arange(10)
print("Array1:" + str(array1))

array2=array1
print("Array2:" + str(array2))
array1[0]=1000
print("Array1:" + str(array1))
print("Array2:" + str(array2))
array2[5]=8888
print("1*********")
print("Array1:" + str(array1))
print("Array2:" + str(array2))
#COPY
array3=array1.copy()
print("2*********")
print("Array1:" + str(array1))
print("Array3:" + str(array3))
array1[2]=444
print("3*********")
print("Array1:" + str(array1))
print("Array2:" + str(array2))
print("Array3:" + str(array3))
array3[0]=7777
print("4*********")
print("Array1:" + str(array1))
print("Array2:" + str(array2))
print("Array3:" + str(array3))

#%%VIEW
array4=array1.view()
print("5*********")
print("Array1:" + str(array1))
print("Array2:" + str(array2))
print("Array3:" + str(array3))
print("Array4:" + str(array4))
array1[9]=9999
print("6*********")
print("Array1:" + str(array1))
print("Array2:" + str(array2))
print("Array3:" + str(array3))
print("Array4:" + str(array4))
print("*********")
array4[8]=5555
print("7*********")
print("Array1:" + str(array1))
print("Array2:" + str(array2))
print("Array3:" + str(array3))
print("Array4:" + str(array4))
array1.shape=2,5
print("8*********")
print("Array1\n:" + str(array1))
print("Array2:\n" + str(array2))
print("Array3:\n" + str(array3))
print("Array4:\n" + str(array4))
array2.shape=5,2
print("9*********")
print("Array1\n:" + str(array1))
print("Array2:\n" + str(array2))
print("Array3:\n" + str(array3))
print("Array4:\n" + str(array4))
array3.shape=2,5
print("10*********")
print("Array1\n:" + str(array1))
print("Array2:\n" + str(array2))
print("Array3:\n" + str(array3))
print("Array4:\n" + str(array4))
array4.shape=1,10
print("11*********")
print("Array1\n:" + str(array1))
print("Array2:\n" + str(array2))
print("Array3:\n" + str(array3))
print("Array4:\n" + str(array4))





























