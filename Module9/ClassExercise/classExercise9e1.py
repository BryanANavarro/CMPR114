# Bryan Navarro
# CMPR114 - Python
# April 17, 2023
# Class Exercise 9 - Object Oriented Programming + Class - Project #5a

# the self is used to represente the instance of the class
# it is used to access variables that belong to that class
class BankAccount:

	def __init__(self, bal):
		self.__balance = bal

	def deposit(self, amount):
		# add the balance
		self.__balance += amount

	def withdraw (self, amount):
		if self.__balance >= amount:
			
			# subtract the balance
			self.__balance -=amount
		
		else:
			print("\nError: Insufficient funds")

	def get_balance(self):
		return self.__balance
