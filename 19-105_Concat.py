# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:45:51 2019

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
orderData3={
        
        "identityNumber":['12345678916','12345678910','12345678914','12345678917'],
        'name':['Gül','Robert','Zuhal','Melisa'],
        'surname':['Zeki','Levin','Duru','Saf']
        }

print("Order Data1:\n" + str(orderData1))
dataFrame1=pd.DataFrame(orderData1)
dataFrame2=pd.DataFrame(orderData2)
dataFrame3=pd.DataFrame(orderData3)
print('********')
print("Concat Operation on horizontal:\n" + str(pd.concat([dataFrame1,dataFrame2,dataFrame3],axis=1)))
print("Concat Operation on vertical with the other usage:\n" + str(pd.concat([dataFrame1,dataFrame2,dataFrame3])))
print("Concat Operation on vertical:\n" + str(pd.concat([dataFrame1,dataFrame2],axis=0)))