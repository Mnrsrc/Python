# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 19:24:06 2019

@author: Munire
"""

countriesSet = {"America","Belgium","Algeria","Denmark","Estonia"}
#Other usage:
citiesSet = set (["Giresun","Şırnak","Hatay","Samsun","Iğdır"])

##Missing usage

print(str(citiesSet))

# Type Finding
print(type(citiesSet))
print(type(countriesSet))

##
print(countriesSet)
print(citiesSet)

#wander
for country in countriesSet:
    print(country)
#wander by keyword

    if "Belgium" in countriesSet:
        print("Belgium country is in the list." )

#ADD
countriesSet.add("Morocco")
print(countriesSet)

#UPDATE

countriesSet.update(["Germany","India","Ireland"])
print(countriesSet)

#LEN FUNCTION
print("Length of Countries Set: "+ str(len(countriesSet)))
print("Length of Cities Set: "+ str(len(citiesSet)))

#REMOVE

countriesSet.remove("India")
print(countriesSet)

#DISCARD: If we want to continue with not error:

countriesSet.discard("india")
print(countriesSet)

#POP
countriesSet.pop()
print(countriesSet)

#CLEAR
countriesSet.clear()
print(countriesSet)

#DEL
del countriesSet 

#We have a error if when we print set because countriesSet is not defined

#print(countriesSet) 






































































