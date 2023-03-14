# Bryan Navarro
# CMPR114 - Python
# February 27, 2023


MAX = 5 # Maximum number

# Initialize an accumulator variable
total = 0.0
average = 0.0
# Explain what we are doing
print('This program calculates the sum of')
print(f'{MAX} numbers you will enter.')

# Get the numbers and accumulate them
for counter in range(MAX):
	number = int(input('Enter a number: '))
	total += number

average = total/MAX
print(f'The total is {total}.\nThe average is {average}')