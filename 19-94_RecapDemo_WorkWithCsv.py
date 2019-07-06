# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 00:48:32 2019

@author: Munire
"""
import pandas as pd
#import numpy as np

notes=pd.read_csv("grades.csv")
notes.columns=["lastName", "firstName", "SSN","test1", "test2", "test3", "test4", "final", "grade"]
print(str(notes))
print(type(notes))
print(notes.head())
print(notes.tail())
print(notes["lastName"])
print("Third data by indexing:\n" +str(notes.iloc[3]))
print("Persons from 5 to 15:\n " + str(notes[5:15]))
