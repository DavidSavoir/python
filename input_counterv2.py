"""

diction={}
while words != '':
  words = input("Enter text: ").split( )
  if not words:
    break
  for word in diction:
    print(word, diction[word]) 
  for word in words:
    if word in diction: 
      print(word, diction[word]) 
    else:
      diction[word] = len(diction)+1
      print(word, diction[word])
   

print("Finished")"""
diction={}
wordset=set()
while True:
  words = input("Enter text: ").split( )
  if not words:
    break
  wordset.update(words)
  for index, word in enumerate(wordset):
      print (word, index+1)
      if word not in diction: 
        diction[word] = len(diction)+1




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