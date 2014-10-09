#
# 1. input counter
#
#2. Write a program that creates an empty set and dict.
diction={}
words=set()
while True:
  for word in words:
    words = input("Enter text: ").split( )
    words.append(word)
    if len(words) > len(diction):
      diction[word]=word
      print(word, diction[word])
  #for x in range(100):
  #if x not in mydic:
    #mydic[x] = x 
  if not words:
    break
  for word in words:
    words.append(word)
    if word not in words:
      diction[word]=word
      print(word, diction[word])
    #print(word, diction[word]) 
  #else:
   #print ("'Word' is NOT in it !")
   #diction[word] = len(diction)+1 
   #print(word, diction[word])

print("Finished")

"""
Enter text: how now brown cow
how 1
now 2
cow 4
brown 3
Enter text: the cow jumped over the moon
brown 3
cow 4
jumped 6
over 7
moon 8
how 1
the 5
now 2
Enter text:
Finished"""

"""    #theset=word()
    #theset = set( )   #  get one going
    #Then you need to add to that set every time:
    #for word in words:  # however you get them
    #theset.add(word)
    if word in diction: ACTION"""
