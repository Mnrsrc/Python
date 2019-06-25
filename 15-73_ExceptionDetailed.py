# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:27:40 2019

@author: Munire
"""

try:
    number=int(input("Please write a number: "))
except (ValueError, ZeroDivisionError):
    print("Type mismatch!!")
except ZeroDivisionError:
    print("Denominator cannot be zero!!!")
print("Done!")