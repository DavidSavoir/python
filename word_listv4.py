# 
# word_list.py Attempt # 1
#
usersentence = input("Input your text: ")
lines = usersentence.strip().split()
counter = 0
currentline = lines[counter]
wordupper = []
wordlower = []

for currentline in usersentence.split():
	counter+=1
	print (counter)
	if currentline.istitle():
		wordupper.append(lines[counter])
	elif currentline.islower():
		wordlower.append(lines[counter])
print (wordupper,"\n",wordlower)