# Bryan Navarro
# CMPR114 - Python
# February 27, 2023

def main():
	names = ['Howard', 'Jamie', 'Jill']
	#element    0         1        2 

	print('\nThe list before the insert or remove functions')
	print(names)

	NameRemove = input('\nEnter the name to remove: ')
	
	names.insert(0,'Joe')
	names.remove(NameRemove)
	
	print('\nThe list after the insert')
	print(names)

main()

def total():
	numbers = [1,2,3,4,5,6,7,8,9,10]
	sum = 0

	for value in numbers:
		sum+=value
	average = sum/len(numbers)
	print("\nThe total is ", sum, " the average is ", average)

	outfile = open('numbers.txt', 'w')
	outfile.write(str(numbers))
	outfile.close()

	print("\nNumbers has been saved.")
total()