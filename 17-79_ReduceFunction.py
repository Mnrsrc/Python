# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:26:37 2019

@author: Munire
"""

numbers=[1,2,3,4,5,6,7,8,9,10]
from functools import reduce

sumOfNumbers=reduce(lambda x,y: x+y,numbers)
print("Sum of numbers from 1 to 10: " + str(sumOfNumbers))