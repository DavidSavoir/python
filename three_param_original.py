__author__ = 'david.savoir'

#three_param.py

import sys

def my_func(*args):
    arglist = []
    for arg in args:
        arglist.append(arg)

    if len(arglist) == 1:
        a = arglist[0]
        b = "b was not entered"
        c = "c was not entered"
        my_print(a, b, c)

    elif len(arglist) == 2:
        a = arglist[0]
        b = arglist[1]
        c = "c was not entered"
        my_print(a, b, c)

    elif len(arglist) == 3:
        a = arglist[0]
        b = arglist[1]
        c = arglist[2]
        my_print(a, b, c)

def my_print(a, b, c):
    print(a)
    print(b)
    print(c)

my_func("test")
my_func("test", "test")
my_func("test", "test", "test")

print(my_func)
