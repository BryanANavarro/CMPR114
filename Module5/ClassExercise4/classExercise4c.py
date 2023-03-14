# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Challenge Exercise 4 - Part 1: Project #3

def main():
	a = add(3,4,5)
	print(f"Total: " + str(total))

	
def add(num1, num2, num3):
	global total
	total = num1 + num2 + num3
	return total


# Call the main function.
main()