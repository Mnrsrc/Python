# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:11:13 2019

@author: Munire
"""

import sqlite3
connection=sqlite3.connect("chinook.db")

cursor=connection.execute("select City,count(*) from customers group by City order by count(*) desc")
for city in cursor:
    print("Cities: " + str(city[0]) + "  "+  str(city[1]))

#%% HAVING CLAUSE

import sqlite3
connection=sqlite3.connect("chinook.db")

cursor=connection.execute("select FirstName,LastName,Email,count(*) from customers group by State having State='SP'  ")
for customer in cursor:
    print("Customers: " + str(customer[0]) + " " + str(customer[1]) + " " + str(customer[2]) + " " + str(customer[3]))