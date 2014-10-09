#
# 1. input counter
#
#2. Write a program that creates an empty set and dict.
diction={}
words=set()
#3. Write a while loop that repeatedly creates a list of words from a line of input from the user.
#4. Loop through the list of words and add each one to the set. 
  #sentence = input('Enter text: ') 
  #originalline = sentence
  #while sentence != '':
  #    lines.append(sentence)
  #    sentence = input('Enter text: ')
while True:
  words = input("Enter text: ").split( )
  #words = input("What is your phrase?")
  if not words:
    break
  for word in words:
    #theset=word()
    #theset = set( )   #  get one going
    #Then you need to add to that set every time:
    #for word in words:  # however you get them
    #theset.add(word)"""
    if word not in words:
      diction.append(word)#
    else:
      print(word, diction[word]) 
      #print(year + '\t' + table[year])
        #myset.add(item)"""
    """if word in diction: 
      print(word, diction[word]) 
    else:
      diction[word] = len(diction)+1
      #for word in sorted(diction.keys()):
      print(word, diction[word])"""
      #4.1. If the set increases in size (indicating this word has not been processed before), 
      #add the word to the dict as a key with the value being the new length of the set.
      #unique_words.append(word) #unique_words.add(word)
      #print (unique_words)
      #if len(diction) > 0  
      #order_found[word] = len(unique_words)
      #print (unique_words) #print what you have in the dict so far and loop to the top --- STOP HERE 

print("Finished")


  #Loop through the list of words and add each one to the set. 
  #Using another loop, display the list of words in the dict along with their value, which represents the order in which they were discovered by the program.
  #If the user presses Enter without any text, print Finished and exit.




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