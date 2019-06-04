# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:47:58 2019

@author: Munire
"""
cologneKinds=["Rose","Lemon","Tobacco","Lavender"]
print(type(cologneKinds))

fileColognes=open("CologneLists.txt","a")

for cologne in cologneKinds:
    fileColognes.write(cologne)
    fileColognes.write("\n")

fileColognes.close()
