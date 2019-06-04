# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:29:30 2019

@author: Munire
"""
##BREAK
cities=["Gaziantep","Van","Hatay","Şırnak","Iğdır","Siirt","İstanbul","Osmaniye","Kastamonu","Niğde","Lefkoşa","Malatya"]
for city in cities:
    if city=="Lefkoşa":
        break
    print(str(city)+ " is belong to Turkey.")
print(str(city) +" is belong to KKTC.")
print("*******")

##CONTINUE
cities=["Gaziantep","Van","Hatay","Şırnak","Iğdır","Siirt","İstanbul","Osmaniye","Kastamonu","Niğde","Lefkoşa","Malatya"]
for city in cities:
    if city=="Lefkoşa":
        continue
    print(str(city)+ " is belong to Turkey.")