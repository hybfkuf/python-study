#!/usr/bin/env python3


class Student(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    #def __repr__(self):
    #    return 'id = '+self.id +', name = '+self.name
    def __str__(self):
        return("__self__")

s = Student('88', 'hybfkuf')
print(s)
print(ascii(s))
