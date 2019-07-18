# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:53:38 2019

@author: Munire
"""

print("Example of stringFunctions:\t" + str('istanbul'.capitalize()))
import pandas as pd

ordersData=pd.read_table('orders.tsv')
print(ordersData)
print(ordersData.columns)
ordersData.columns=['orderId','quantity','itemName','choiceDescription','itemPrice']
print(ordersData.tail(10))
print(ordersData.itemName)
print('*****')
print(ordersData['itemName'].head(20))
ordersData.itemName=ordersData.itemName.str.lower()
ordersData.choiceDescription=ordersData.choiceDescription.str.lower()
print('*****')
print(ordersData.tail()[['itemName','choiceDescription']])

print(ordersData.itemName.value_counts(dropna=False))
print("Which orders related to steak:\n" + str(ordersData.itemName.str.contains('steak')))
print('*****')
print("How many related to steak in orders:\n" + str(ordersData.itemName.str.contains('steak').value_counts(dropna=False)))
ordersData.choiceDescription=ordersData.choiceDescription.str.replace('[','').str.replace(']','')
print(ordersData.choiceDescription)


print(ordersData.choiceDescription.value_counts(dropna=False))
ordersData.choiceDescription=ordersData.choiceDescription.str.replace('NaN','UNCERTAIN')
print('*****')
ordersData['choiceDescription'].fillna(value='UNCERTAIN',inplace=True)
print(ordersData.choiceDescription.value_counts(dropna=False))
