# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:43:05 2019

@author: Munire
"""

import pandas as pd
ufoData=pd.read_csv("http://bit.ly/uforeports")
print(ufoData)
print("Shape of data:\n" + str(ufoData.shape))
ufoData=ufoData.dropna()
print("Shape of data with dropna:\n" + str(ufoData) + "\n Shape of Data with dropna\n:" + str(ufoData.shape))

ufoData=ufoData.dropna(how="any")
print("New shape:\n" + str(ufoData.shape))

ufoData=ufoData.dropna(how="all")
print("Newest:\n" + str(ufoData.shape))

#GENERAL USAGE:
ufoData=ufoData.dropna(subset=['City','Colors Reported'],how="any")
print("Without not null cities and colors:\n" + str(ufoData))

ufoData=ufoData.dropna(subset=['Shape Reported','Colors Reported'],how="all")
print("Without not null shapes and colors:\n" + str(ufoData))