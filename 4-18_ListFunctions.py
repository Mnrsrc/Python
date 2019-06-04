# -*- coding: utf-8 -*-

sehirler=list(("İstanbul","Adana","Bursa","Zonguldak","Denizli"))
#APPEND
sehirler.append("Yalova")
#TO LIST
print(sehirler)
#LEN
print(len("Lenght of Cities:"+ str(sehirler)))
#REMOVE
sehirler.remove("İstanbul")
print(sehirler)
#CLEAR
sehirler.clear()
print(sehirler)
#COUNT

sehirler=list(("İstanbul","Adana","Bursa","Zonguldak","Denizli"))
print("Number of Denizli: "+ str(sehirler.count("Denizli")))

#INDEX
print("Index of Adana: "+ str(sehirler.index("Adana")))

#POP
sehirler.pop(3)
print("Final State: " + str(sehirler))

#INSERT
sehirler.insert(2,"Balıkesir")
print(sehirler)

#REVERSE
sehirler.reverse()
print("Reverse of Cities:" + str( sehirler))

sehirler2=sehirler
#COPY

sehirler3=sehirler.copy()
sehirler.append("Edirne")
###ARRAYS ARE OF THE REFERENCE TYPE
print(sehirler2)
print(sehirler3)

#EXTEND
regions=list(("Bahçelievler","Adalar","Burgazada"))
sehirler.extend(regions)
print("Cities and their regions: "+ str(sehirler))

#SORT
sehirler.sort()
print("The order of cities and their regions: " + str(sehirler))
#SORT - REVERSE
sehirler.sort()
sehirler.reverse()
print("The reverse order of cities and their regions:  " + str(sehirler))

