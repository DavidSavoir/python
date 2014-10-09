# 
# word_list.py Attempt # 1
#
usersentence = input("Input your text: ")
lines = usersentence.split()
print (lines)
counter = 0
currentline = lines[counter]
wordupper = []
wordlower = []

while counter < len(lines):
	counter +=1
	if lines[counter].istitle():
		wordupper.append(lines[counter])
	elif lines[counter].islower():
		wordlower.append(lines[counter])
print (wordupper,"\n",wordlower)