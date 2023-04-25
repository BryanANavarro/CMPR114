# Bryan Navarro
# CMPR114 - Python
# April 24, 2023
# Class Exercise 10 - Inheritance class Project #1

class A:
	def one(self):
		print("1")
	def two(self):
		print("2")

class B(A): # Class B is inheriting from class A
	def three(self):
		print("3")
	def four(self):
		print("4")

# only sees objects in A
a1 = A()
a1.one()
a1.two()

# only sees objects in B
b1 = B()
b1.three()
b1.four()

b1.one()
b1.two()
b1.three()
b1.four()
