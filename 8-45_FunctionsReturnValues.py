# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:58:48 2019

@author: Munire
"""

#%%KIND 1
def CalculateCircleArea(radius,pi):
    return pi*radius*radius
  
area=CalculateCircleArea(4,3)
print(area)
#%%KIND 2
def CalculateCircleArea2():
    pi=3.14
    radius=float(input("Write a radius for Circle, please: "))
    return radius*radius*pi
circleArea=CalculateCircleArea2()
print("Area of Circle: ", circleArea)
    
 

