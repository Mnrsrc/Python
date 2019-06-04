# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:10:17 2019

@author: Munire
"""
import json

dataCosmetic='{"Perfume":"Versace","Cream":"Farmasi","Deodorant":"Nivea"}'
print(type(dataCosmetic))

jsonCosmetic=json.loads(dataCosmetic)
print(type(jsonCosmetic))

print(jsonCosmetic["Perfume"])

cosmeticProducts={
        "Shampoo":"Pantene",
        "Cleanser":"Este Lauder",
        "Toothpaste":"Signal"
        }
print(type(cosmeticProducts))
cosmeticJsonData=json.dumps(cosmeticProducts)
print(cosmeticJsonData)

name="Münire"
jsonName=json.dumps(name)
print(json.dumps("Münire"))
print(jsonName)
