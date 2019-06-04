# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:58:30 2019

@author: Munire
"""

number1=int(input("1.ci sayıyı giriniz: "))
number2=int(input("2.ci sayıyı giriniz:"))
number3=int(input("3.cü sayıyı giriniz:"))

if (number1>=number2) & (number1>=number3):
    print("En büyük sayı: " + str(number1))
    
elif (number2>=number1) & (number2>=number3):
    print("En büyük sayı: " + str(number2))
    
else:
    print("En büyük sayı: " + str(number3))