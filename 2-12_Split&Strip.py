# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:50:59 2019

@author: Munire
"""
data="Münire ŞİRECİ 14 İSTANBUL ADIYAMAN"
print(data.split())

data="Münire ŞİRECİ 14 İSTANBUL ADIYAMAN  "
print(data.split(" "))

data="Münire;ŞİRECİ;14;İSTANBUL;ADIYAMAN"
print(data.split())

data="Münire;ŞİRECİ;14;İSTANBUL;ADIYAMAN"
print(data.split(";"))

data="         Münire  ŞİRECİ  14  İSTANBUL  ADIYAMAN  ".strip()
print(data.split())

data="         Münire  ŞİRECİ  14  İSTANBUL  ADIYAMAN  ".strip()
print(data.split(" "))