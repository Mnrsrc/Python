# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:48:23 2019

@author: Munire
"""
from scipy import mat

matrix1= mat('[1,2,3;4,5,6;7,8,9]')
matrix2=mat('[2,4,6;8,10,12;14,16,18]')
sumMatrix=matrix1+matrix2
print("Sum of Matrixs: " + str(sumMatrix))