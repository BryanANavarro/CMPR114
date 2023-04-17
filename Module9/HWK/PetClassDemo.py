# Bryan Navarro
# CMPR114 - Python
# April 17, 2023
# Homework Assignment 7 - Project #1b

import PetClass

def main():
	name = input("\nEnter a name for the pet: ")
	type = input("Enter type of pet: ")
	age = int(input("Enter the age of the pet: "))
	
	Pet1 = PetClass.Pet(name, type, age)

	PetClass.Pet.set_name = name
	PetClass.Pet.set_animal_type = type
	PetClass.Pet.set_age = age
	

	print(f"\nThe name of the pet is {Pet1.get_name()}. The pet type is {Pet1.get_animal_type()}. The pet's age is {Pet1.get_age()}")
main()