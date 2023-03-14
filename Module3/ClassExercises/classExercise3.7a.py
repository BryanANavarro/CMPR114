# Bryan Navarro
# CMPR114 - Python
# February 27, 2023

def main1():
	prodNums =['V475','F987', 'Q143', 'R688'] #list of values
	search = input('\nEnter a product: ')

	if search in prodNums: #determines if the product# is in the list
		print(search,'was found on the list ')
	else:
		print(search,'was not found on the list')
main1()

def main2():
	nameList = []

	again = 'y'

	while again == 'y':
		name = input('\nEnter a name: ')
		nameList.append(name) #appends the names in a list format

		print('\nDo you want to add another name?')
		again = input('y = yes. Hit any other key for NO: ')
		print()

		print(' here are the names you enetered: ')
		for name in nameList: #loop through each name in nameList
			print(name)
		
		# Writing the list to a text file
		
		# Open the file first
		outfile = open('names.txt', 'w')
		# file.write function to write to text file
		outfile.write(str(nameList))
		# Make sure to close the file in order to save the file
		outfile.close()
		
		print('File with list of names has been saved.')
main2()