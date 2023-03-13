# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Challenge Exercise 4 - Part 1: Project #2

def main():
	information()

# Definition of information function.
# Allows user to enter information.
def information():
	firstName = input("\nEnter your first name: ")
	lastName = input("\nEnter your last name: ")
	address = input("\nEnter your address: ")
	city = input("\nEnter your city: ")
	state = input("\nEnter your state: ")
	zipCode = input("\nEnter your zip code: ")

	print(f"\nName: {firstName} {lastName}")
	print(f"\nAddress: {address} {city}, {state} {zipCode}")

main()