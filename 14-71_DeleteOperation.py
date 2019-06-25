# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:42:33 2019

@author: Munire
"""

import sqlite3
connection=sqlite3.connect("chinook.db")
cursor= connection.execute("""Delete from genres where Name like '%&%' """)
connection.commit()
cursor2=connection.execute("""select Name from genres """)
print("***Genres ***")
for genre in cursor2:
    print(genre[0])

connection.close()