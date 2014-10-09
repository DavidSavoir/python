import random

ranvalue = random.randint(1, 99)
print (ranvalue)

while True:
    guessnumber = int(input("Guess a number:"))
    if guessnumber > ranvalue:
        print("Too low")
    elif guessnumber < ranvalue:
        print("Too high")
    else:
        print("You guessed it !")
        break

"""
Making sure your secret number betwee 1 and 99 inclusive is a requirement.
Neither 0 nor 100 should ever be picked.

ranvalue = int(random.randint(0, 100))

is problematic for another reason:  since randint returns
an int, you should not need to feed its output to int( ) for
an int.  That's like going str(input("prompt: ")) when input()
only returns strings.

"""
