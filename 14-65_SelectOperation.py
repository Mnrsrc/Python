# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:32:34 2019

@author: Munire
"""

import sqlite3
connection=sqlite3.connect("chinook.db")
cursor=connection.execute("select * from albums ")
for album in cursor:
    print("Album lists: " + album[1])
connection.close()

#%% QUERY 2
connection=sqlite3.connect("chinook.db")
cursor=connection.execute("select * from tracks")
for trackComp in cursor:
    print("Track and Composers: " ,str(trackComp[1]) + "\n" + str(trackComp[5] ))
connection.close()

#%% QUERY 3
import sqlite3
connection=sqlite3.connect("chinook.db")
cursor=connection.execute("select FirstName,LastName,Company from customers where company='Apple Inc.' ")
for customer in cursor:
    print("Customers: " +str(customer[0]) + "\n"+ str(customer[1]) + "\n" + str(customer[2]))
    print("********")
connection.close()

#%%QUERY 4
import sqlite3
connection=sqlite3.connect("chinook.db")
cursor=connection.execute("select  FirstName,LastName from employees where City='Calgary' and Title='Sales Support Agent'")
for employee in cursor:
    print("Employees: " + str(employee[0]) + "\t" + str(employee[1]))

connection.close()