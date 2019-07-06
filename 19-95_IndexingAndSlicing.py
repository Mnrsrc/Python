# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 23:52:13 2019

@author: Munire
"""

import pandas as pd
notes=pd.read_csv("grades.csv")
notes.columns=["lastName","firstName","SSN","Test1","Test2","Test3","Test4","Final","Grade"]
print(notes)
print("Final notes by indexing:\n" + str(notes.loc[:,"lastName"]) )
