# Bryan Navarro
# CMPR114 - Python
# February 27, 2023

# while loop flag
flag = 'y'
# constant for max tempature
MAX_TEMP = 102.5

sum = 0.0
temperature = 0.0
average = 0.0
counter = 0

while temperature <= MAX_TEMP and flag == 'y':
	temperature = float(input("\nEnter the temperature for today: "))
		
	# when temperature is too high, goes into this loop
	while temperature > MAX_TEMP:
		print('\nThe temperature is too high.')
		temperature = float(input('Enter a temperature under 102.5: '))

	sum += temperature
	counter+=1
	print('\nThe temperature is acceptable.')
	if counter == 4:
		break;
	flag = input('\nDo you want to add another temperature? y-yes or n-no? ')

average = sum / counter
print("\nSum: " + str(sum))
print("\nAverage: " + str(average))