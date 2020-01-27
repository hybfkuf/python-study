#!/usr/bin/env python3

def decorator(func):
    def wrapFunc():
        print("Before decorator")
        func()
        print("After decorator")
    return wrapFunc

@decorator
def my_func():
    print("my_func")

my_func()
print(my_func.__name__)
