# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:05:05 2019

@author: Munire
"""
myList=["America","UK",5,2,4,7]
filterList=list(filter(lambda x:x!="America",myList))
print("Filtered List: "+str(filterList))
print(type("AMERİCA"))
#%%EXAMPLE 2
list2=[]
for i in myList:
    if type(i)!=str:
        list2.append(i)
        filteredList2=list(filter(lambda y:y>5 , list2))
        print("Filtered List: " + str(filteredList2))
    else:
        continue
