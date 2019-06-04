# -*- coding: utf-8 -*-

class MathFunction:
    def __init__(self,number1,number2):
        self.x=number1
        self.y=number2
    def sum(self):
        return self.x+self.y
    def substract(self):
        return self.x-self.y
    def multiply(self):
        return self.x*self.y
    def divide(self):
        return self.x/self.y
    def mode(self):
        return self.x%self.y
#    IT DOESNT WORK THİS USAGE!!!
#math1=MathFunction()
#print("Multiplication of numbers: " + math1.multiply(1,2))
math1=MathFunction(10,5)
print("Division of numbers: ", str(math1.divide()))
print("Mode of numbers: " + str(math1.mode()))

    