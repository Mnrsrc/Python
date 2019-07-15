# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:40:59 2019

@author: Munire
"""

import pandas as pd
ufoData=pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")
#THE OTHER LINK:
ufoData2=pd.read_csv('http://bit.ly/uforeports')
print(ufoData)
print("Columns:\n" + str(ufoData.columns))
ufoData.columns=["city","colorsReported","shapeReported","state","time"]
print("Last 5 data:\n" + str(ufoData.tail()))
print("Data of cities:\n" + str(ufoData["city"]))
print("Some of data:\n" + str(ufoData[["city","colorsReported","time"]].head(1000)))
print("NaN Data:\n" + str(ufoData.isnull()))
print("Not null data:\n" + str(ufoData.notnull().tail(50)))
print("Sum of null cities' data:\n" + str(ufoData["city"].isnull().sum()))
print("Sum of all data:\n" + str(ufoData.isnull().sum()))
print("Other data of NaN cities"+str(ufoData[ufoData.city.isnull()]))
print("Not null colors data:\n" + str(ufoData[ufoData.colorsReported.notnull()][["city","colorsReported"]]))
