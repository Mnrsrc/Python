# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:15:09 2019

@author: Munire
"""

import sqlite3
connection=sqlite3.connect("chinook.db")
cursor=connection.execute("""select FirstName,LastName,BillingCity,Total from customers inner join invoices
                          on customers.CustomerId=invoices.CustomerId """)
for bill in cursor:
#    print("First Name: " + str(bill[0]) + " Last Name: " + str(bill[1]) + " City: " + str(bill[2]) + 
#    " Total: " +str(bill[3])""")
    print("First Name: " + str(bill[0]))
    print("Last Name: " + str(bill[1]))
    print("City: " + str(bill[2]))
    print("Total: " +str(bill[3]))
    print("*******")
connection.close()
    