dogs=[]
class Dog():
	def __init__ (self, name, breed):
			self.name = name 
			self.breed = breed

			#instance = Dog(name,breed)
			#print (dogs)

while True:
	name = input("Name:")
	if name == "": 
		sys.exit()
	else: 
		breed = input("Breed: ")
		dogs.append(Dog(name,breed))
		print (Dog(name,breed))