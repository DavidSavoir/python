dogs = {}
import sys

class Dog():
    def __init__(self, name, breed):
        #instance = Dog(name, breed)
        #dogs.update({name, breed})


        print(dogs)

while True:
    name = input("Name:")
    breed = input("Breed: ")
    #print (name, breed)
    #Dog(name, breed)
    dogs.update({self.name, self.breed})
    print("*" * 15)
    if name == "":  #Blank name still
        sys.exit()

    #is the list being filled ?