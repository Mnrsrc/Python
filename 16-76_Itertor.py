# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:20:14 2019

@author: Munire
"""

shampoobrands=["Pantene","Head&Shoulders","Blendax","Elidor","Bioblas"]
myiterator=iter(shampoobrands)
print("Shampoo Brands: ")
print(next(myiterator))
print(next(myiterator))
#%% WITH FOR LOOP
print("Shampoo Brands: ")
for brand in shampoobrands:
    print(brand)
