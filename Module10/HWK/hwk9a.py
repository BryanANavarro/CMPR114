# Bryan Navarro
# CMPR114 - Python
# April 24, 2023
# Homework 13 - Inheritance - Project #1

class Employee:
	def __init__ (self, name, number):
		self.__name = name
		self.__number = number

	def set_name(self, name):
		self.__name = name

	def set_number(self, number):
		self.__number = number

	def get_name(self):
		return self.__name

	def get_number(self):
		return self.__number

class Supervisor(Employee):
	def __init__(self, name, number, salary, bonus):
		super().__init__(name, number)
		self.__salary = salary
		self.__bonus = bonus

	def set_salary(self, salary):
		self.__salary = salary
	
	def set_bonus(self, bonus):
		self.__bonus = bonus

	def get_salary(self):
		return self.__salary

	def get_bonus(self):
		return self.__bonus

name = input("\nEnter name: ")
number = input("Enter number: ")
salary = float(input("Enter salary: "))
bonus = float(input("Enter bonus: "))

supervisor = Supervisor(name, number, salary, bonus)

print(f"\nName: {supervisor.get_name()}")
print(f"Number: {supervisor.get_number()}")
print(f"Salary: ${supervisor.get_salary():,.2f}")
print(f"Bonus: ${supervisor.get_bonus():,.2f}")