# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:47:50 2019

@author: Munire
"""

import pandas as pd
import numpy as np
series=pd.Series()
print(series)

data=np.array(["Singapore", "United States","United Kingdom"])
series2=pd.Series(data)
print("Numpy Data:\n" + str(series2))

withOurIndexSeries=pd.Series(data,index=[1,2,3])
print("Numpy Data With Our Indexing:\n" + str(series2))

dictionary={"Math":50,"English":60 ,"Physics":20}
print("Dictionary: " + str(dictionary))
seriesDictionary=pd.Series(dictionary)
print("Usage Series with dictionary:\n" + str(seriesDictionary))
seriesIndex=pd.Series(dictionary,index=["Math","English","Physics"])
seriesIndex2=pd.Series(dictionary,index=["1","2","3"])
seriesIndex3=pd.Series(dictionary,index=["English","English","Physics"])
print("Dictionary are indexing with Series:\n" + str(seriesIndex))
print("Dictionary are indexing with Series:\n" + str(seriesIndex2))
print("Dictionary are indexing with Series:\n" + str(seriesIndex3))
print("Note of Maths: " + str(seriesIndex["Math"]))

series3=pd.Series(10)
print(series3)
series4=pd.Series(8,index =[5,6,7,8])
print(series4)