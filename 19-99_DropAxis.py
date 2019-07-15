# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:25:56 2019

@author: Munire
"""

import pandas as pd
movies=pd.read_csv("C:\Python\Temel\Pandas\Pandas\imdb_1000.csv")
print(movies)
print(movies.columns)
movies.columns=["starRating","title","contentRating","genre","duration","actorList"]
print(movies.columns)
print(movies.head())
#DROP COLUMN
movies=movies.drop("actorList",axis=1)
print("****")
print(movies)
#DROP ROW
movies=movies.drop(0,axis=0)
print("Delete from row=0:\n" + str(movies))
#LIST OF ROWS TO DELETE
#rowsToDrop=[0,1,3,5,7,9,11,13,15,17,19] #IT DOES NOT WORK. BECAUSE row=0 already has been deleted
rowsToDrop=[1,3,5,7,9,11,13,15,17,19]
print("Final State:\n"+ str(movies.drop(rowsToDrop,axis=0)))
print(movies)