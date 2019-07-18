# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:47:57 2019

@author: Munire
"""
import pandas as pd

orderData1={
        "identityNumber":['12345678910','12345678911','12345678912','12345678913'],
        "name":["Andrew","Sophia","Begüm","Mert"],
        "surname":['Kaya','Mercan','Işık','Gök']
        }
orderData2={
        
        "identityNumber":['12345678912','12345678910','12345678914','12345678915'],
        'name':['Şule','Mehmet','David','Marta'],
        'surname':['Kaan','Kalkmaz','Blue','Green']
        }
print("Order Data1:\n" + str(orderData1))
dataFrame1=pd.DataFrame(orderData1)
dataFrame2=pd.DataFrame(orderData2)
print('********')
print("Order Data with DataFrame:\n" + str(dataFrame1))
print('********')
print("Inner Join Operation:\n" + str(pd.merge(dataFrame1,dataFrame2,on='identityNumber',how='inner')))
print("Left Join Operation:\n" + str(pd.merge(dataFrame1,dataFrame2,on='identityNumber',how='left')))
print('Right Join Operation:\n' + str(pd.merge(dataFrame1,dataFrame2,on="identityNumber", how='right')))