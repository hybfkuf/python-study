#!/usr/bin/env python3

def deco(func):
    def wrapFunc():
        print("Before decorator")
        func()
        print("After decorator")
    return wrapFunc

def my_func():
    print("my_func")

my_func = deco(my_func)
my_func()
