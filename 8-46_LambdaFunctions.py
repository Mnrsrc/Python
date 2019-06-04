# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:36:26 2019

@author: Munire
"""

#VOLUME OF SPHERE
volumeSphere=lambda radius,pi=3:(4/3)*pi*radius*radius*radius
result=volumeSphere
print("Volume of Sphere: ",result(4))
#%%KIND 2 
volumeSphere2= lambda radius=float(input("Write a radius value, please: ")),pi=3:(4/3)*pi*radius*radius*radius
print("Volume of Sphere: "+ str(volumeSphere2()))
