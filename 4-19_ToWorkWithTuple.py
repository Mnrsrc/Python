# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:46:57 2019

@author: Munire
"""

tupleListe=()
list=[]
tupleListe=(1,2,3,4,5,6,7,8,9,"Edirne","Van","Gaziantep")
list=[1,2,3,4,5,6,7,8,9,"Edirne","Van","Gaziantep"]

#They can write nested
tupleListe=(1,2,3,4,5,6,7,8,9,"Edirne","Van","Gaziantep",["Uşak",0,2])
list=[1,2,3,4,5,6,7,8,9,"Edirne","Van","Gaziantep",("Uşak",0,2)]
print(type(list))
print(type(tupleListe))
print("Tuple List: "+str(tupleListe))
print("List: "+str(tupleListe))

#Update process is not work in Tuple list

#tupleListe[0]=5
#print(str(tupleListe))

list[0]=5
print(str(list))

#Indexing
print("Last but one item: "+str(list[-2]))
print("Last but fourth item: "+ str(tupleListe[-5]))

#Fragmentation
print("One to two item in Tuple List: "+str(tupleListe[1:2]))
print("One to two item in  List:"+str(list[1:2]))

#NOTE
#Tuple value is not written   alone.If it's written we must write  comma(,) next to item

tupleDeger=("Münire",)
print(str(tupleDeger))
print(type(tupleDeger))





















