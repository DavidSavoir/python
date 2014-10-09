__author__ = 'david.savoir'
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
#print(lst)
#print('*' * 80)
word_list = ''.join(lst).replace('\n', '').replace("'", '').replace(".", '').split(' ')

#word_list = ' '.join(lst).split(' ')
#print(word_list)
#print('*'*80)
tup = ()
diction = {}

for word in word_list:
    diction[word] = len(word)

#print(diction)
#print('*'*80)

t_dict = {}
for key, value in diction.items():
    if value in t_dict:
        t_dict[value] += 1
    else:
        t_dict[value] = 1

print(t_dict)
print('*'*80)
print('')

max_count = max(t_dict.values())
screen_height = 20

count_per_line = float(max_count)/screen_height

counts = t_dict.values()

def column_height(count):
    return int(round(count / count_per_line))

def key_func(x):
    word_length, count = x
    return word_length

for line_num in range(screen_height, 0, -1):
    row_minimum_count = int(line_num * count_per_line)
    # print y axis labels e.g. 400 -|
    for word_length, count in sorted(t_dict.items(), key=key_func):
        if count > row_minimum_count:
            print('***', end='')
        else:
            print('   ', end='')
    print()

print('---1--2') # print x axis
