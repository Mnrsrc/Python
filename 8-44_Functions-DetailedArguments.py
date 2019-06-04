# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:57:41 2019

@author: Munire
"""

#%%PARAMETERLESS FUNCTION

def sayHello():
    print("Hello! ")

sayHello()

#%%PARAMETIRIZED FUNCTION

def sayHello2(name):
    print("Hi",name)
    
sayHello2("Ali")
sayHello2("Zeynep")
sayHello2("Berkay")
sayHello2("Yusuf")
#%% KINDS 1
def sayHello3(name="User"):
    print("Dear " + name)
sayHello3()
sayHello3("Ceren")
#%%KINDS 2
def sayHello4(name,surname):
    print("Dear " + name+" "+surname)
##IT DOESN'T WORK!!!!!
#IT MUST BE PARAMETER VARIABLE
#sayHello4()

sayHello4("Veli","Konak")
#%%KINDS 3
def sayHello5 (name="Deren" ,surname="Yeşil"):
    print("Dear " + name+ " " + surname)
sayHello5("Elif","Mezur")
sayHello5()
sayHello5("Ümit")
#%%KINDS 4
##IT DOES NOT WORK !!!
##Default parameter is must write or parameter is not empty.
#def sayHello6(name="User",surname):
#    print("Dear " + name +" "+ surname)
#sayHello6("Ferhunde")

def sayHello6(name, surname="Yorulmaz"):
    print("Dear " + name +" "+ surname)
sayHello6("Gamze")
##IT DOES NOT WORK!!!
#Default parameters are must be in the end
#def sayHello7(name="Turan",surname):
#    print("Dear" + name+ " "+ surname)
#sayHello7("Bağcıklı")













































