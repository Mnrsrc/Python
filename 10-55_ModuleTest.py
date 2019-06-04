# -*- coding: utf-8 -*-

import ModuleWriting
#IT DOESN'T WORK!!!
#import _10-54_Inheritance

print("Brand of Shampoo: ", ModuleWriting.shampoo) 

print("Name of cream: " + str(ModuleWriting.cream))
print("Name of cream: " + str(ModuleWriting.cream["name"]))
print("Price of Shampoo: " , str(ModuleWriting.calculate(0.75,24)))

#%%KIND 2 
import ModuleWriting as mod
print(mod.shampoo)
#%%KIND 3
from ModuleWriting import calculate,cream
print("Price: " , calculate(1,40))

brand=cream["brand"]
print(brand)
