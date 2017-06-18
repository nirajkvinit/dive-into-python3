#!/usr/bin/python3
class Person:

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def __init__(self, name, age):
        #self.name = name
        #self.age = age
        self.setName(name)
        self.setAge(age)

    def printPerson(self):
        print("Name: " + str( self.getName() ))
        print("Age: " + str(self.getAge() ))

person = Person("Niraj", 33)
person.printPerson()
person2 = Person("Pankaj", 30)
person2.printPerson()
