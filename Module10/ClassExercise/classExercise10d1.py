# Bryan Navarro
# CMPR114 - Python
# April 24, 2023
# Class Exercise 10 - Inheritance class Project #4-1

class Automobiles:

	def __init__(self, make, model, mileage, price, doors):
		self.__make = make
		self.__model = model
		self.__mileage = mileage
		self.__price = price
		self.__doors = doors

	# these are the mutator methods

	def set_make(self, make):
		self.__make = make
	
	def set_model(self, model):
		self.__model = model

	def set_mileage(self, mileage):
		self.__mileage = mileage

	def set_price(self, price):
		self.__price = price

	def set_doors(self, doors):
		self.__doors = doors

	# these are the accessor methods

	def get_make(self):
		return self.__make
	
	def get_model(self):
		return self.__model
	
	def get_mileage(self):
		return self.__mileage
	
	def get_price(self):
		return self.__price

	def get_doors(self):
		return self.__doors

class Truck(Automobiles):
	def __init__(self, make, model, mileage, price, doors):
		Automobiles.__init__(self, make, model, mileage, price, doors)

class SUV(Automobiles):
	def __init__(self, make, model, mileage, price, doors):
		Automobiles.__init__(self, make, model, mileage, price, doors)