#three_param.py

import sys
#a, b, c = argv
#import pdb
#pdb.set_trace()


def my_func(*args):
    #print (a,b,c)
    #len(sys.argv) < 1:
    #print ("No value was entered")
    arglist = []
    #for arg in sys.argv:
    for arg in args:
        arglist.append(arg)

    if len(arglist) == 1:
        a = arglist[0]
        b = "b was not entered"
        c = "c was not entered"
        #print (a,b,c)
        return a,b,c
    elif len(arglist) == 2:
        a = arglist[0]
        b = arglist[1]
        c = "c was not entered"
        #print (a,b,c)
        #my_print(a, b, c)
        return a,b,c

    elif len(arglist) == 3:
        a = arglist[0]
        b = arglist[1]
        c = arglist[2]
        #print (a,b,c)
        return a,b,c
        #my_print(a, b, c)

"""
def my_print(a, b, c):
    print(a)
    print(b)
    print(c)
"""
my_func("test")
my_func("test", "test")
my_func("test", "test", "test")

print (my_func)

# need to return the function, however it returns None'

"""
Create a new Python source file named three_param.py.
Write a program that has a function named my_func with three parameters, 'a', 'b', and 'c'. The first parameter is required, and the second two parameters have the default values of 'b was not entered' and 'c was not entered'. The function must print the value of each parameter.
In your program, call my_func three times. The first time, just provide a value for the first parameter. The second time, provide values for the first and second parameters. The third time, provide values for all three parameters.
In your program, print the function itself."""

