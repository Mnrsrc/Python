# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:00:09 2019

@author: Munire
"""

import sqlite3
connection=sqlite3.connect("chinook.db")

cursor=connection.execute("select * from media_types order by Name")
for media in cursor:
    print(media)

connection.close()

#%% QUERY 2
import sqlite3
connection=sqlite3.connect("chinook.db")
cursor=connection.execute("Select BillingCity,BillingCountry,Total from invoices order by BillingCity, BillingCountry desc,Total desc")
for bill_cities in cursor:
    print("Cities:" + str(bill_cities[0]) + " Countries:" + str(bill_cities[1]) + " Total:"+ str(bill_cities[2]))