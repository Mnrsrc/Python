#Not Dynamic

#country1="America"
#counrty2="England"
#country3="Germany"
#
#print(country1)
#print(counrty2)
#print(country3)

##
#countries=["America","England","Germany"]
#print(countries)
#print("2nd country: "+ countries[2])
##APPEND
#countries.append("Turkey")
#print(countries)
##REMOVE
#countries.remove("America")
#print("European Countries: "+ str(countries))
#
##UPDATE
#countries[0]="Turkey"
#countries[2]="Germany"
#print("Europen Countries: "+ str(countries))

#LIST CONSTRUCTOR
cities= list(("İstanbul","Bursa","İzmir"))
print(cities)
print("Belong to Aegean: " + str(cities[2]))
print("Length of List: "+ str(len(cities)))
cities.append("Muğla")
print(cities)
cities.remove("İstanbul")
cities[0]="Çanakkkale"
print(cities)