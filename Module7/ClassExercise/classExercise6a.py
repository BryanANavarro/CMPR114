# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Challenge Exercise 6 String Manipulation- Project #1

def main():
	# Get a string from the user.
	user_string = input("Enter a string: ")

	print("This is what I found about that string: ")

	# Test the string.
	if user_string.isalnum():
		print("The string is alphanumeric.")
	if user_string.isdigit():
		print("The string contains only digits.")
	if user_string.isalpha():
		print("The string contains only alphabetic characters.")
	if user_string.isspace():
		print("The string contains only whiespace characters.")
	if user_string.islower():
		print("THe letters in the string are all lowercase.")
	if user_string.isupper():
		print("The letters in the string are all uppercase.")

# Call the string
main()