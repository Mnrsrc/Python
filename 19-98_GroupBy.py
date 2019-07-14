# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 23:44:10 2019

@author: Munire
"""

import pandas as pd
movies=pd.read_csv('imdb_1000.csv')

print(movies.head())
print(movies.columns)
movies.columns=['starRating','title','contentRating','genre','duration','actorList']
print( "First film in the list:\n" +str(movies.loc[0]))
print("Average of all films:\t" +str(movies.duration.mean()))
print("Average of films to according to content rating:\n" +str(movies.groupby('contentRating').duration.mean()))