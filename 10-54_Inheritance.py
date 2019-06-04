# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:14:57 2019

@author: Munire
"""

class Person:
    def __init__(self,firstName,lastName,identitiyNumber,age,length,weight):
        self.firstName=firstName
        self.lastName=lastName
        self.identitiyNumber=identitiyNumber
        self.age=age
        self.length=length
        self.weight=weight

class Student(Person):
    def __init(self,studentNumber,studentCertificate,scholarship):
        self.studentNumber=studentNumber
        self.studentCertificate=studentCertificate
        self.scholarship=scholarship

class Employee(Person):
    def __init__(self,salary,insurance):
        self.salary=salary
        self.insurance=insurance


#zeynep=Student("Zeynep","Kaçar","12345678910",17,165,48,147,"Yes",400)
#buket=Employee("Buket","Yeşil", "12345678911",25,168,55,3000,True)
#zeynep=Student()
#print("Scholarship of Zeynep: " + str(zeynep.scholarship(400)))
    