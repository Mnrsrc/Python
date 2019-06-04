# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:07:05 2019

@author: Munire
"""

import sqlite3

connection=sqlite3.connect("chinook.db")
cursor=connection.execute("select Name from playlists where Name like '%music%'")
for playlist in cursor:
    print("Playlists:" + str(playlist[0]))