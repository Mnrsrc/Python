# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:26:50 2019

@author: Munire
"""

numbers=[0,1,2,3,4,5,6,7,8,9,10]
cubeOfNumbers=[]
for number in numbers:
    cubeOfNumbers.append(number*number*number)
    print(number*number*number)
#%%WITH LAMBDA FUNCTION and MAPPING
cubeOfNumbers=list(map(lambda number:number*number*number,numbers))
print(str(cubeOfNumbers))
#%% --2nd
squareOfNumbers=lambda number:number**2
squareLists=list(map(squareOfNumbers,numbers))
print(squareLists)