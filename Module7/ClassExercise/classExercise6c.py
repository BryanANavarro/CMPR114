# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Challenge Exercise 6 String Manipulation - Project #3

# This program demonstrates how to tokenize strings

def main():
	# Strings to tokenize
	str1 = 'one two three four'
	str2 = '10:20:30:40:50'
	str3 = 'a/b/c/d/e/f'

	# display the tokens in each string.
	display_tokens(str1, ' ')
	print()
	display_tokens(str2, ':')
	print()
	display_tokens(str3, '/')

# The display_tokens function displays the tokens in a string.
# The data parameter is the string to tokenize and the delimiter
# parameter is the delimiter.

def display_tokens(data, delimiter):
	tokens = data.split(delimiter)
	for item in tokens:
		print(f'Token: {item}')
# Execute the main function.
if __name__ == '__main__':
	main()