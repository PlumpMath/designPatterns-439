#!/bin/python

# singleton is one of the simplest and well-known Creational design patterns.

"""
Singleton provides you a mechanism to have one, and only one, object of a given type and provides a global point of access.
Singletons are typically used in cases such as logging or database operations, where there is a need to have only one instance that i available across the application to avoid confricting requests o the same resource.

Requisites
    1. We will allow the creation of only one instance of the Singleton class
    2. If an instance exists, we will serve the same object again

UML
------ Singleton -------
| - instance : Singleton   ----->
| - Singleon()             ----->
| + instance() : Singleton ----->
------------------------
"""

class Singleton(object):
    __data="none"
    def __new__(cls): # special method to instantiate objects
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    def getData(self):
        return self.__data

    def setData(self,newData):
        self.__data=newData

s = Singleton()
print("Object s created", s)
print("Data: ", s.getData())

s.setData("asd")

s1 = Singleton()
print("Object s1 created", s1)
print("Data: ", s1.getData())
