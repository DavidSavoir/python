#doggies.py

dogs = []
import sys


class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        #print(self.breed, self.name )

    #instance = Dog(name,breed)
    #print (dogs)


"""
class Dog():
	def whatever(self, name, breed):
			instance = Dog(name,breed)
			print (dogs)
"""

while True:
    name = input("Name:")
    if name == "":
        sys.exit()
    else:
        breed = input("Breed: ")
        dogs.append(Dog(name, breed))
        Dog(name, breed)



"""

dogs=[]
import sys
while True:
	name = input("Name:")
	breed = input("Breed: ")
	print (name, breed)
	print ("*"*15)
	if name == "": #Blank name still 
		sys.exit()
class Dog():
	def __init__ (self, name, breed):
			instance = Dog(name,breed)
			dogs.append(instance)

			print (dogs)


Dog(name, breed)
"""

"""
#Write a class named Dog. Dog's __init__() method should take two parameters, name and breed, in addition to the implicit self.
#Bind an empty list to a dogs global variable (dogs should not be an attribute of the Dog class).
Using a while loop, get user input for name and breed. The loop should terminate when the user enters a blank name.
For each name and breed entered, create an instance of the Dog class with name and breed as arguments. Append the object to the dogs list.
Each time around the loop, print the current dogs list (the name and breed of each dog).
Below is an example of possible output from running the program.

Name: Snoopy
Breed: Beagle
DOGS
0. Snoopy:Beagle
****************************************
Name: Marmaduke
Breed: Great Dane
DOGS
0. Snoopy:Beagle
1. Marmaduke:Great Dane
****************************************
"""