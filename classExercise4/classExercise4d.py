# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Challenge Exercise 4 - Part 1: Project #4

def main():
	num1 = int(input("\nEnter the first number: "))
	num2 = int(input("\nEnter the second number: "))
	num3 = int(input("\nEnter the third number: "))

	a = sum(num1, num2, num3)
	b = average(num1, num2, num3)

	print(f"\nSum: {sum}")
	print(f"\nAverage: {average}")


	
def sum(num1, num2, num3):
	global sum
	sum = num1 + num2 + num3
	return sum

def average(num1, num2, num3):
	global average
	average = (num1 + num2 + num3)/3
	return average

# Call the main function.
main()