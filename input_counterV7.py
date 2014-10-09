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
  else: 
    for word in words: 
      lenset=len(wordset)
      wordset.add(word)
      if len(wordset)>lenset:
        diction[word]=len(wordset)
    for k,v in diction.items():
      print (k,v)

"""
       for each word in the input text:
set a variable equal to the length of the set
add word to the set
if the length of the set is greater than the length of the "old" set:
add the word to the dict 
for k, v in words.items():
print(k, v)


    wordset.add
    for index, word in enumerate(wordset):
      if len(wordset)>len(words)
        diction[len(wordset)]=word

  #  dict
  
  #for index, word in enumerate(wordset):
  #  if word not in diction: 
  #    diction[word] = len(diction)+1





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