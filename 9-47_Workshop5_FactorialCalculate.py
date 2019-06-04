

# -*- coding: utf-8 -*-
def CalculateFactorial():
        number=int(input("Please write a number value: "))
        if number<0:
            print("Please write a positive number!!! ")
        elif number==0:
                number=1
                print("Factorial of 0: ", str(number))
        else:
            result=1
            for x in range(1,number+1):
                result=x*result
            print("Factorial of "+ str(number)+": "+  str(result))
            return result
    
    

CalculateFactorial()







