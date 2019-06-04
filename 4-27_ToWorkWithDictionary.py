# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:55:13 2019

@author: Munire
"""

EnglishToTurkishDictionary= {
        
        "author":"yazar",
        "ball":"top",
        "cow":"inek",
        "delete":"eklemek"
        }
print("Words: "+str(EnglishToTurkishDictionary))

HexNumberDictionary={
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F",
        }
print("Hexadecimal Number Code: " +str(HexNumberDictionary))

BinaryCode={
        
        "0001":1,
        "0010":2,
        "0011":3,
        "0100":4,
       " 0101":5,
       "1000001":65
        }
print("Binary Number: " +str(BinaryCode))

#OTHER USAGE
EnglishToTurkishDictionary2=dict(elephant="fil", fill="doldurmak")

#  ERROR: 17="0011"

print("Dictionary: "+ str(EnglishToTurkishDictionary2))


#ERROR
#print(str(EnglishToTurkishDictionary[1]))
#LIST

print("Author:"+str(EnglishToTurkishDictionary["author"]))

#UPDATE
EnglishToTurkishDictionary["delete"]="silmek"

print("Delete:" + str(EnglishToTurkishDictionary["delete"]))

#ADD
HexNumberDictionary[16]="0010"
print(HexNumberDictionary)

#LENGTH
print("Length of EnglishToTurkishDictionary2: " + str(len(EnglishToTurkishDictionary2)))

#DELETE
del(EnglishToTurkishDictionary["author"])
print(EnglishToTurkishDictionary)



















































































