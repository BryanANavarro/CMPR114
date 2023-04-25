# Bryan Navarro
# CMPR114 - Python
# April 24, 2023
# Class Exercise 10 - Inheritance class Project #2

class AnimalType:
	def eats(self):
		print("This animal likes to eat?")
class rabbits(AnimalType):
	def munch(self):
		print("Carrots")

class birds(rabbits):
	def munch1(self):
		print("Seeds")
class dogs(rabbits):
	def munch2(self):
		print("Hot dogs")

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

#here we have the Bird Object inheriting
#from two different classes
BirdObject = AnimalType()
BirdObject = birds()

BirdObject.eats()
BirdObject.munch1()

DogObject = AnimalType()
DogObject = dogs()

DogObject.eats()
DogObject.munch2()