#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
#    def __str__(self):
#        print("__str__")
#        return "Student(%s, %d)" %(self.name, self.age)
    def __repr_(self):
        print("__repr__")
        return "Student(%s, %d)" %(self.name, self.age)

var1 = Student("Jack", 18)
var2 = ['jonas', '23']

print("\n=== type: ====")
print(var1)
print(var2)
print('\n')

print("=== value: ====")
print(var1)
print(var2)
print('\n')
