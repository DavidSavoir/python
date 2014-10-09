# 
# word_list.py Attempt # 1
#
usersentence = input("Input your text: ")
lines = usersentence.strip().split()
print (lines)
counter = 0
currentline = lines[counter]
wordupper = []
wordlower = []

while counter < len(lines):
	counter +=1
	if currentline.istitle():
		wordupper.append(lines[counter])
	elif currentline.islower():
		wordlower.append(lines[counter])
		break
print (wordupper,"\n",wordlower)