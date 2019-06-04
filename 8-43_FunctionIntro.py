# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:12:40 2019

@author: Munire
"""
country="Norveç"

##PARAMETERLESS FUNCTION
print(country.upper())
##PARAMETIRIZED FUNCTION
print(country.startswith("ç"))

#%% EXAMPLE
cities=("İstanbul","Rize","Kastamonu","Osmaniye","Mersin","Nevşehir","Malatya")
for x in cities:
    if(x.startswith("M")):
        print("Cities are starting with 'M': ",x)
        continue
 #%% FALSE RETURN   
    ##RETURN FALSE, Because cities are not starting with 'S'
for x in cities:
    if(x.endswith("s")):
        print("Cities are ending with 's':",x)
        continue
print("Any cities are not ending with 's'")

      

        
