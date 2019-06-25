# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:10:38 2019

@author: Munire
"""
import numpy as np
#default value is 50.
numbers=np.linspace(1,10)
print("Numbers of between 1-10 in fifties: " + str(numbers))

numbers2=np.linspace(1,10,10)
print("Numbers of between 1-10 in tens: " + str(numbers2))
#????
from numpy import pi
myValue=np.linspace(0,2*pi,100)
print("\n" + str(myValue))
print("Sinus value" +str(myValue)+ ": " + str(np.sin(myValue)))