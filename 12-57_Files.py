# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:40:22 2019

@author: Munire
"""
#x is being wrritten once
#f=open("Toothpastelist.txt","x")
#f=open("Toothpastelist.txt","w")
f=open("Toothpastelist.txt","r")
#f=open("Toothpastelist.txt","a")
#print(f.read())
print(f.readline(10))
print(f.readline())
print(f.readline())

for x in f:
    print(x)
#f=open("Toothpastelist2.txt","xt")
f=open("BinaryList","xb")