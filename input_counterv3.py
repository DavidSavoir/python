#
# 1. input counter
#
#2. Write a program that creates an empty set and dict.
lines=[]
diction={}
emptyset=()
startset=()
unique_words=[]
words=()
uin=()
#3. Write a while loop that repeatedly creates a list of words from a line of input from the user.
#4. Loop through the list of words and add each one to the set. 
  #sentence = input('Enter text: ') 
  #originalline = sentence
  #while sentence != '':
  #    lines.append(sentence)
  #    sentence = input('Enter text: ')
while True:
    words = uin(input("What is your phrase? ").split( )
    #words = input("What is your phrase?")
    if words == emptyset:
        break
    for word in words:
        if word in diction:
            diction[word] += 1
        else:
            diction[word] = 1
for word in sorted(diction.keys()):
    print(word, diction[word])
    #unique_words.append(word) #unique_words.add(word)
    #print (unique_words)
    #if the set got larger
    #order_found[word] = len(unique_words)
    #print (unique_words) #print what you have in the dict so far and loop to the top

print("Finished")