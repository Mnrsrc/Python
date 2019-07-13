# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 00:12:58 2019

@author: Munire
"""

import pandas as pd
movies=pd.read_csv("imdb_1000.csv")
#print("Movies:\n"+ str(movies))
print("All columns of data:\n" + str(movies.columns))
movies.columns=["starRating","title","contentRating","genre","duration","actorList"]
print("*****")
print(movies.head())
print("First 100 movies the best rate of movies:\n" + str(movies[:100][['title','starRating']]) )
print("First 5 movies" + str(movies[['title','genre']].head()))
print("\n Last 20 movies the worst content rate of movies:\n" + str(movies.loc[:,"contentRating"].tail()))
print("Durations bigger than 150:\n" + str(movies
                                                          [movies['duration']>154]
                                                          [['title','genre','duration']]))

print("The rate of movies  8.5 to 9.0\n:" + str(movies[(movies['starRating']>8.5)&(movies['starRating']<9.0)]
                                                        [['title','starRating']]))

print("The rate of movies bigger than 8.5 or less than 9.0:\n" + str(movies[(movies['starRating']<8.5) | (movies['starRating']>9.3)]
                                                            [['title','starRating']]))


