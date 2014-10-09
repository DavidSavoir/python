#
# 1. input counter
#
#2. Write a program that creates an empty set and dict.
diction={}
words=set()
while True:
  words = input("Enter text: ").split( )
  if not words:
    break
  for word in words:
    #theset=word()
    #theset = set( )   #  get one going
    #Then you need to add to that set every time:
    #for word in words:  # however you get them
    #theset.add(word)"""
    #if word in diction: ACTION
    if word in words:
      print ("'Word' is in it !")
      words.append(word)
      #b = set('alacazam')
      print(word, diction[word]) 
    else:
      print ("'Word' is NOT in it !")
      diction[word] = len(diction)+1 
      print(word, diction[word])

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
