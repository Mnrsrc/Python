# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:59:49 2019

@author: Munire
"""

asianCountries={"China","Russia","Korea","Turkey"}
europeCountries={"Sweden","Switzerland","England","Netherlands","Turkey"}
africaCountries={"Morocco","Tunisian","Saudi Arabia","Turkey"}

print(asianCountries&africaCountries&europeCountries)
#OTHER USAGE
print(asianCountries.intersection(europeCountries).intersection(africaCountries))