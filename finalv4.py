"""#Call the program with an argument, it should treat the argument as a filename, and process the content of the file.
#calling with argument = sys.argv
"""
"""In other words, import sys at the top, and then have your script open
sys.argv[1] instead of declaration.txt.  It should still work.   The string
'declaration.txt' then need not appear anywhere in the source code."""

import sys
#f = open(sys.argv[1]).read()
#f = open('C:\Users\david.savoir\Documents\GitHub\python\Pythoncode\declaration.txt').read()
f = open(r'C:\Users\david.savoir\Documents\GitHub\python\Pythoncode\declaration.txt', 'r')

#f = open("declaration.txt", 'r')
    #f = open('declaration2.txt').read()"""

"""The output should be about the same as what's shown depending on how you deal with the "&".
Your wordlist contains "'Men," suggesting punctuation cleaning is not thorough.

An example of punctuation cleaning from the Lessons was more like:

for symbol in string.punctuation:
    target = target.replace(symbol, "")

Splitting with no argument is a far better strategy than splitting on " "
because .split( ) consumes all whitespace, including newlines.

I would suggest going straight to words from the passage like this:

words = f.read().split()

and then:

for word in words:

but instead of len(word) you could have a function that strips out any punctuation there
and then:

for word in words:
   true_length = get_length(word)  # function to NOT count puctuation as part of length
   t_dict[true_length] = t_dict.get(true_length, 0) + 1  # something like this

Just an idea.  Your numbers are quite a bit different than those shown."""

lst = []
"""
#new_string = re.sub('^a-zA-Z0-9\n', ' ', f)
#    for line in new_string.readlines():
"""
lst.append(f)
print(lst)
print('*' * 80)
words = f.read().split()
print ("***PRINTING WORDS NOW ***")
print (words)

word_list = re.sub(r'[^a-zA-Z]', '').word_list
word_list = ''.join(lst).replace('\n', '').replace("'", '').replace(".", '').split(' ')

"""
word_list = ' '.join(lst).split(' ')
"""
print(word_list)
print('*'*80)
tup = ()
diction = {}
#i=1
for words in word_list:
    diction[words] = len(words)
"""
    #print (i, diction[i])
    #i=i+1
"""
print(diction)
print('*'*80)
t_dict = {}
for key, value in diction.items():
    if value in t_dict:
        t_dict[value] += 1
    else:
        t_dict[value] = 1

#print(t_dict)
for k,v in t_dict.items():
    print (k,v,)

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
