#
# 1. input counter
#
#2. Write a program that creates an empty set and dict.
lines=[]
startdict={}
#3. Write a while loop that repeatedly creates a list of words from a line of input from the user.
#4. Loop through the list of words and add each one to the set. 


	#usertext = input("Enter a text: ")
	#textwords = usertext.split()
	#textlength = len(textwords)"""


	# while textwords != 0 or textlength != counter: ==> results in index out of range again
	#while len(textwords):
	#	startset.append(textwords)
	#	print (startset[textlength])
sentence = input('Enter text: ') 
originalline = sentence
while sentence != '':
    lines.append(sentence)
    sentence = input('Enter text: ')
# If the set increases in size (indicating this word has not been processed before), 
    if sentence != originalline: 
    # add the word to the dict as a key with the value being the new length of the set.	
        print ("different") # This being a test to see if my reasoning was correct. 
        #startdict = {originalline.difference(sentence):len(lines)}
        #The above statement does not work as you can't assign variables to a dictionary. I seem to be having troubles getting into the logic of this one
        #any hints would be greatly appreciated. 
else:
	print ("Finished!") # 6. If the user presses Enter without any text, print Finished and exit.
#5. Using another loop, display the list of words in the dict along with their value, 
# which represents the order in which they were discovered by the program."""
print('Your lines were:')
for sentence in lines:
    print(sentence)



