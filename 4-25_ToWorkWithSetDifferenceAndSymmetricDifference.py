# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:20:05 2019

@author: Munire
"""

asianCountries={"China","Russia","Korea","Turkey"}
europeCountries={"Sweden","Switzerland","England","Netherlands","Turkey"}
africaCountries={"Morocco","Tunisian","Saudi Arabia","Turkey"}

print(asianCountries - europeCountries)
#OTHER USAGE
print("The difference of Europian Countries from Africian Countries: "+str(europeCountries.difference(africaCountries)))

##SYMMETRİC DIFFERENCE
print(asianCountries ^africaCountries)
#OTHER USAGE
print("The symmetric difference of Asian Countries from Europian Countries:" + str(asianCountries.symmetric_difference(europeCountries)))