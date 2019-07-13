# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 01:02:33 2019

@author: Munire
"""

import pandas as pd
movies=pd.read_csv('imdb_1000.csv')

print(movies)
print(movies.head())
print(movies.columns)
movies.columns=['starRating','title','contentRating','genre','duration','actorList']
print(movies.columns)
print(movies.tail())
print("Film duration is less than 60 minutes:\n" + str(movies.query('duration<90')
                                                                [['title','genre','duration']]))