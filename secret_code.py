#secret code.py
new_letter=[]

userinput = input("Message:")#.splitlines())

#print(userinput)

#secretstring=''.join(chr(ord(c)+1)) for c in userinput
#print(secretstring)

"""for letter in userinput:
	if letter == " ":
		print ("space")
		diction[letter]=len(wordset)"""



for letter in userinput:
	#new_letter.add(chr(ord(letter)+1))
	#print (new_letter)
	#new_letter.add((ord(letter)+1))
	new_letter.append(chr(ord(letter)+1))


secretstring=''.join(new_letter)

print(secretstring)