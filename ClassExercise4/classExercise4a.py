# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Challenge Exercise 4 - Part 1: Project #1

def main():
	# Call the texas function.
	texas()
	# Call the california function.
	california()

# Definition of the texas function.
# It creates a local variable named birds.
def texas():
		birds = int(input("\nEnter the amount of birds Texas has: "))
		print(f"\nTexas has {birds} birds.")

# Definition of the california function. 
# It creates a local variable named birds.
def california():
		birds = int(input("\nEnter the amount of birds California has: "))
		print(f"\nCalifornia has {birds} birds.")
	# Call the main function.

main()
