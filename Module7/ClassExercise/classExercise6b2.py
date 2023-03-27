# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Challenge Exercise 6 String Manipulation - Project #2b

# This program gets a password from the user and validates it

import classExercise7b

def main():
	# Get a password from the user.
	password = input("Enter your password: ")

	# Validate the password
	while not classExercise7b.valid_password(password):
		print("That password is not valid.\n")
		password = input("Enter your password: ")
	
	print("That is a valid password.")

# Call the main function.
if __name__ == '__main__':
	main()