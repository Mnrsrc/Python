# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:26:07 2019

@author: Munire
"""

import pandas as pd
ufoData=pd.read_csv('ufo.csv')
print(ufoData)
print(ufoData.columns)
ufoData.columns=['city','color','shape','state','time']
print(ufoData.head())
#It does not this way:
#ufoData=ufoData['color'].fillna(value='UNCERTAIN',inplace=True)
ufoData['color'].fillna(value='UNCERTAIN',inplace=True)
print("UFOs according to colors:\n"+ str(ufoData['color'].value_counts(dropna=False)))
