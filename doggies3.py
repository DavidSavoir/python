__author__ = 'david.savoir'

class Dog(object):

    def add(self, name, breed):
        self.__dict__['name'] = name
        self.__dict__['breed'] = breed
        for k,v items in self.__dict__.items():
            print k,v

    def __repr__(self):
        return '{} {} '.format(self.__dict__['name'],
                                    self.__dict__['breed'])

while True:
    dog = Dog()
    name = input("Name:")
    breed = input ("Breed:")
    dog.add(name, breed)
    print (dog) #newline > not working
    print("*" * 15)
    if dog.name == "":  #Blank name still
        sys.exit()