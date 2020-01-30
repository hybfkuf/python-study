#!/usr/bin/env python3

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapFunc():
        print("Before decorator")
        func()
        print("After decorator")
    return wrapFunc()

def my_func():
    print("my_func")

my_func()
print(my_func.__name__)

