class Dog:
	animal = 'dog'
	def __init__(self, breed, color):

		self.breed = breed
		self.color = color

Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print ('Rodger details:')
print ('Rodger is a', Rodger.animal)
print ('Breed:', Rodger.breed)
print ('Color: ', Rodger.color)
print ('\n')

print ('Buzo details:')
print ('Buzo is a', Buzo.animal)
print ('Breed:', Buzo.breed)
print ('Color: ', Buzo.color)
print ('\n')

print("Accessing class varable using class name")
print(Dog.animal)
