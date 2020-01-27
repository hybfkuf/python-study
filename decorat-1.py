#!/usr/bin/env python3

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I'm doing some boring work before executing a_func()")
        a_func()
        print("I'm doing some boring work after executing a_func()")
    return wrapTheFunction


def two():
    print("second function")

two=a_new_decorator(two)
two()
