# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:40:51 2019

@author: Munire
"""

class MathCalculation:
#    number1=float(input("Please write first number value: "))
#    number2=float(input("Please write second number value: "))
    def sum(self,number1,number2):
        result=number1+number2
        return result
#    print("Sum of numbers: ",str(number1+number2))
    
    def substraction(self,number1,number2):
        result=number1-number2
        return result
#    print("Difference of numbers: ",str(number1-number2))
    
    def multiply(self,number1,number2):
        result=number1*number2
        return result
#    print("Multiplication of numbers: ",str(number1*number2))
    
    def divide(self,number1,number2):
        result=number1/number2
        return result
#    print("Division of numbers: ",str(number1/number2))
    
    def mode(self,number1,number2):
        result=number1 % number2
        return result
#    print("Mode of numbers: ",str(number1%number2))
    
math1=MathCalculation()
math2=MathCalculation()
print("Sum of numbers= " + str(math1.sum(7,8)))
print("Difference of numbers: " + str(math2.substraction(15,2)))