#!/usr/bin/python3
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))

person = Person("Niraj", 33)
person.printPerson()
