#!/usr/local/bin/python3
"""Program to locate the first space in het input string."""

s = input("Please enter a string: ")
pos = 0
for c in s:
    if c ==" ":
    	print("First space occured at position", pos)
    	break
    pos +=1
else:
	print("No spaces in that string")