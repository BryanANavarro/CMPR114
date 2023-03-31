# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Homework Assignment 7 - Project #7

import pickle

# main function
def main():
	fileName = "vegetables.dat"
	vegetables = loadFile(fileName)

	while True:
		menu()
		
		choice = int(input("\nEnter choice: "))

		if choice == 1:
			for vegetable, price in vegetables.items():
				print(f"{vegetable:<10}{price:>10.2f}")
		
		elif choice == 2:
			vegetable = input("Enter vegetable name: ").upper()
			price = float(input("Enter vegetable price: "))
			vegetables[vegetable] = price
			print("\nRecord saved.")
		elif choice == 3:
			vegetable = input("Enter vegetable name: ").upper()
			if vegetable not in vegetables:
				print("\nERROR: Vegetable name not found")
				continue
			price = float(input("Enter vegetable price: "))
			vegetables[vegetable] = price
			print("\nRecord saved.")
		elif choice == 4:
			vegetable = input("\nEnter vegetable name you would like to delete: ").upper()
			if vegetable in vegetables:
				del vegetables[vegetable]
			else:
				print("\nERROR: Vegetable name not found")
		
		elif choice == 0:
			break
		
		else:
			choice = int(input("\nINVALID INPUT. Enter a number from the menu: "))

# reads file into vegetables 
def loadFile(fileName):
	try:
		with open(fileName,'rb') as inFile:
			vegetables = pickel.load(inFile)
			return vegetables
	except:
		return dict()

# writes file 
def writeFile(fileName, vegetables):
	with open(fileName, 'wb') as outFile:
		pickl.dump(vegetables, outFile)

# Displays the menu
def menu():
	print("\n1. List of Vegetables")
	print("2. Add a new vegetable")
	print("3. Change the Price of an existing vegetable")
	print("4. Delete an existing vegetable")
	print("0. Exit")
	

# Call the main function.
if __name__ == '__main__':
	main()