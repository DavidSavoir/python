
f = open("declaration.txt", 'r')

lst = []


for line in f.readlines():
        lst.append(line)
print (lst)
print ('*' * 80)
word_list = ' '.join(lst).split(' ')
print (word_list)
print ('*'*80)
tup=()
diction={}
#i=1
for words in word_list:
    diction[words]=len(words)
    #print (i, diction[i])
    #i=i+1
print (diction)
print ('*'*80)



print("400 - |")
print("    - |")



"""
Length    Count
       1       16
       2      267
       3      267
       4      169
       5      140
       6      112
       7       99
       8       68
       9       61
      10       56
      11       35
      12       13
      13        9
      14        7
      15        2

1) Find unit (267 = max)
2) 80 = width (max/80 = units)= 1 star =>
3) At 8 star level > print out Y/N > if not print space
One column = 3 stars


  400 -|
       |
       |
       |
       |
  300 -|
       |
       |   ******
       |   ******
       |   ******
  200 -|   ******
       |   ******
       |   *********
       |   ************
       |   ************
  100 -|   ***************
       |   ******************
       |   ************************
       |   ***************************
       |   ******************************
    0 -+-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
       | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16


Hints for Program Design:
You don't need to be quite as sophisticated as the standard solution in your scaling and labeling, but you should consider how to handle inputs where the counts are smaller (e.g. in the 5-50 range). The real trick is working out what should be printed in each column for every row--it would be much easier to print the histogram sideways! (meaning that's not an acceptable alternative).

Because our vertical (y-axis) scale is in increments of 20, we don't see representations of word lengths of fewer occurrences than 20 (the 12- through 15-character words).
"""


