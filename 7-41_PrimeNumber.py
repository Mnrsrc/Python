# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:32:41 2019

@author: Munire
"""

number=int(input("Lütfen bir sayı giriniz: "))
isPrimeNumber=True
for x in range(2,number-1):
    if (number%x)==0:
        isPrimeNumber=False
        break   
    
if isPrimeNumber:
#OTHER USAGE--->if isPrimeNumber==True:
    print("ASAL SAYI")
else:
    print("ASAL SAYI DEĞİL")
