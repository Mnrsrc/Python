# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:47:47 2019

@author: Munire
"""
import sqlite3
def InsertOperation():
    connection=sqlite3.connect("chinook.db")
    connection.execute("""insert into employees(FirstName,LastName,Title) 
                        values ('Münire','ŞİRECİ','Software Developer')""")
    connection.commit()
    connection.close()
    
InsertOperation()