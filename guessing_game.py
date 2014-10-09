import random
ranvalue = int(random.randint(0, 100))
while True:
	guessnumber = int(input("Guess a number:"))
	if guessnumber > ranvalue:
		print("Too low")
	elif guessnumber < ranvalue: 
		print ("Too high")
	else: 
		print ("You guessed it !")
		break
