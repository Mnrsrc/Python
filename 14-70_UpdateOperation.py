# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:04:06 2019

@author: Munire
"""

import sqlite3
def UpdateOperation():
    connection=sqlite3.connect("chinook.db")
    connection.execute("""update media_types 
                       set Name='MP3 file'
                       where Name like '%MPEG%'""")
    connection.commit()
    connection.close()

UpdateOperation()