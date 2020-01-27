#!/usr/bin/env python3

class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return("__repr__")

class B(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return("__str__")

a = A('hybfkuf', 23)
b = B('Jonas', 18)

print(a)
#print(b)
print(globals())
