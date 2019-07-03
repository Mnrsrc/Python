# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 00:44:46 2019

@author: Munire
"""
import pandas as pd
dataFrame=pd.DataFrame()
print("My empty DataFrame:\n" + str(dataFrame))
numbers=[[0,2,4,6,8,10],[1,3,5,7,9,11]]
dataFrame2=pd.DataFrame(numbers)
print("****")
print(dataFrame2)

customers={
        "passportNumber":["1111111","2222222","3333333","4444444"],
        "name":["Emma","Johnson","Marry","Dimitra"],
        "country":["US","England","France","Greece"],
        "age":[45,23,12,25]
    
        }
dataFrame3=pd.DataFrame(customers,index=['c1','c2','c3','c4'])
print("All of Customers:"+str(dataFrame3))
print("Countries of all customers:\n" + str(dataFrame3["country"]))
print("****")
#Fetchs Error!!!
#print(dataFrame3[1])
#DELETE 1
del dataFrame3["age"]
print(dataFrame3)
print("****")
#DELETE 2
dataFrame3.pop("passportNumber")
print(dataFrame3)