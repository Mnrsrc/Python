# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:21:02 2019

@author: Munire
"""




def add(number1,number2):
    result=number1+number2
#    print("S of numbers: " + number1+number2)
#    writeResult()
    return result

def substract(number1,number2):
    return number1-number2
def multiply(number1,number2):
    return number1*number2
def divide(number1,number2):
    return number1/number2
#def inputValue():
#      number1=float(input("Write a first number value, please: "))
#      number2=float(input("Write a second number value, please: "))
    
    

#def writeResult():
#    print(result)
login=int(input("What do you want to do?" + "\n" + "1:Addition \n2:Substraction \n3:Multiplication \n4:Division   "))
if login==1:
    #   inputValue()
    number1=float(input("Write a first number value, please: "))
    number2=float(input("Write a second number value, please: "))
    print("Sum of numbers: " + str(add(number1,number2)))
elif login==2:
    number1=float(input("Write a first number value, please: "))
    number2=float(input("Write a second number value, please: "))
    print("Difference of numbers: " + str(substract(number1,number2)))
elif login==3:
    number1=float(input("Write a first number value, please: "))
    number2=float(input("Write a second number value, please: "))
    print("Multiplication of numbers: " + str(multiply(number1,number2)))
elif login==4:
    number1=float(input("Write a first number value, please: "))
    number2=float(input("Write a second number value, please: "))
    print("Divide of numbers: " + str(divide(number1,number2)))
else:
    print("Please write between 1-4 numbers: " )





    

