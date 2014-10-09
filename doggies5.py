__author__ = 'david.savoir'

class Dog(object):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # is there still a use for __repr__ and if so how does it compare to __str__ ???
       # %r, %d, %s
    def __repr__(self):
        return '{} {} '.format(self.name,self.breed)


dogs = [] # does it matter where this is put ?

while True:

    # get name and breed or exit

    input_name = input("Name:")
    if input_name == "":
        sys.exit()
    input_breed = input ("Breed:")
    #dog = Dog(name, breed) # if I remove this line, I won't get "TypeError: __init__() missing 2 required positional arguments: 'name' and 'breed"
    newdog = Dog(input_name, input_breed)  # this is where __init__ is triggered
    dogs.append(newdog)
    # then some printing, looping over dogs
    print ("Dogs")
    for dognumber, dog in enumerate(dogs): #TypeError: 'Dog' object is not iterable
        print(dognumber,".",dog)
    print ("*"*80)

"""
Rather than define an add method, have __init__ construct your new Dog instance:

    def __init__(self, n, b):
        self.name = n
        self.breed = b

I suggest __str__ rather than __repr__ for your "{}:{}" output, note colon added.

Then remember the global list dogs.

dogs = [ ]
while True:
    # get name and breed or exit
    newdog = Dog(input_name, input_breed)  # this is where __init__ is triggered
    dogs.append(newdog)
    # then some printing, looping over dogs

This is the basic workflow, with Dog instances being appended to a global list that
is then looped over for printing purposes.  An enumeration might be used given how
the example report contains numbers.
"""


"""
while True:

    dog.add(name, breed)
    print (dog)
    print("*" * 15)
    if dog.name == "":
        sys.exit()
"""