# Bryan Navarro
# CMPR114 - Python
# March 1, 2023

number = 0
sum = 0.0

# number is positive
while number >= 0:
	# Get input from user
	number = int(input("\nEnter a positive number or enter a negative number to end: "))
	# if negative number, break from loop
	if number < 0:
		print(f"\nYou have entered {number} which is a negative number.")
		break
	else:
		sum+=number

print(f"\nThis is the sum of all numbers: {sum}")