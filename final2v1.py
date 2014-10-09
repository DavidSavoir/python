#Call the program with an argument, it should treat the argument as a filename, and process the content of the file.
#calling with argument = sys.argv

import sys
import os
#import pdb
#pdb.set_trace()
#myFile = open(sys.argv[1])
import re
import operator
#f = open("declaration.txt", 'r')
f = open('declaration2.txt').read()


lst = []
"""new_string = re.sub('^a-zA-Z0-9\n', ' ', f)
for line in new_string.readlines():"""
lst.append(f)
print(lst)
print('*' * 80)
word_list = ''.join(lst).replace('\n', '').replace("'", '').replace(".", '').split(' ')
#word_list = ' '.join(lst).split(' ')
print(word_list)
print('*'*80)
tup = ()
diction = {}
#i=1
for words in word_list:
    diction[words] = len(words)
    #print (i, diction[i])
    #i=i+1
print(diction)
print('*'*80)
t_dict = {}
for key, value in diction.items():
    if value in t_dict:
        t_dict[value] += 1
    else:
        t_dict[value] = 1

print(t_dict)
print('*'*80)
print('')

for key, value in sorted(t_dict.items(), key=operator.itemgetter(1), reverse=True):
    if value == 10:
        print('10 -|', ' '*((key*2)-2), " *")
    if value == 9:
        print('09 -|', ' '*((key*2)-2), " *")
    if value == 8:
        print('08 -|', ' '*((key*2)-2), " *")
    if value == 7:
        print('07 -|', ' '*((key*2)-2), " *")
    if value == 6:
        print('06 -|', ' '*((key*2)-2), " *")
    if value == 5:
        print('05 -|', ' '*((key*2)-2), " *")
    if value == 4:
        print('04 -|', ' '*((key*2)-2), " *")
    if value == 3:
        print('03 -|', ' '*((key*2)-2), " *")
    if value == 2:
        print('02 -|', ' '*((key*2)-2), " *")
    if value == 1:
        print('01 -|', ' '*((key*2)-2), " *")
    #print(key, '-', value)
print('        1 2 3 4 5 6 7 8 9 10')


"""

    #for word
    #lst = line.split()
    #print (lst)
    #for word in lst:
    #print (lst)
"""

"""
Length Count
 1 16
 2 267
 3 267
 4 169
 5 140
 6 112
 7 99
 8 68
 9 61
 10 56
 11 35
 12 13
 13 9
 14 7
 15 2
 """
