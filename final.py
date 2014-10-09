#Call the program with an argument, it should treat the argument as a filename, and process the content of the file.
#calling with argument = sys.argv


import sys
import os
#import pdb
#pdb.set_trace()
#myFile = open(sys.argv[1])

f = open("declaration.txt", 'r')

lst = []

# The program reads all the input, splitting it up into words, and computes the length of each word.
# Punctuation marks should not be included as a part of the word, so "it's" should be counted as a
# three-character word, and "final." should be counted as a five-character word.

#f.readline().split("X Points = ")[1].strip()
for line in f.readlines():
        lst.append(line)
print(lst)
print('*' * 80)
word_list = ''.join(lst).replace('\n', '').split(' ')
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
#Counter(diction).most_common(3) # find the equivalent of 'collections' Counter below ???
counter = 0
occurence = 0
#while counter < 10:

#Keep track of just length
#for key, value in diction.items():
#    counter += 1

#    if value == counter:
#        occurence += 1
#    print(counter, occurence)

t_dict = {}
for key, value in diction.items():
    if value in t_dict:
        t_dict[value] += 1
    else:
        t_dict[value] = 1

print(t_dict)
"""

    #for word
    #lst = line.split()
    #print (lst)
    #for word in lst:
    #print (lst)
"""
f.close()
	#for line in myInputFile.readlines():
	#print line


#The example text includes a "word" of zero length (the "&"); your solution should handle this.

#When all input has been processed ,the program should print a table showing the word count for each of the word lengths that has been encountered.
# Your tutor will run your code against several standardized inputs to verify the correctness of your logic.
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
