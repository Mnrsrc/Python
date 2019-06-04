# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:34:38 2019

@author: Munire
"""

inputValue=float(input("Lütfen bir sayı giriniz: "))
if inputValue==0:
    print("Girdiğiniz sayı 0'dır.")
elif inputValue<0:
    print("Girdiğiniz sayı negatiftir.")
else:
    print("Girdiğiniz sayı pozitiftir.")