# 
# Guess.py: A guessing game
#

secret = 12

guess = int(input ("Guess a number: "))
guessnumber = 1

while guess != secret:
	if guessnumber < 5:
		if guess > secret:
			guess = int(input ("Guess lower: "))
			guessnumber +=1
		elif guess < secret:
			guess = int(input ("Guess higher: "))
			guessnumber +=1
	else:
		print ("Sorry the number was ", secret)
		break
print ("Hooray, you guessed correctly !")
