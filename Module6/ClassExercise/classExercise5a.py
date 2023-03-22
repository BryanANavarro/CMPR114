# Bryan Navarro
# CMPR114 - Python
# March 20, 2023
# Challenge Exercise 5 - Project #1


def writeInput():
	
	firstName = input("\nEnter first name: ")
	lastName = input("Enter last name: ")
	age = int(input("Enter age: "))

	infoFile = open('info.txt', 'w')

	infoFile.write("\nFirst Name: " + firstName)
	infoFile.write("\nLast Name: " + lastName)
	infoFile.write("\nAge: " + str(age) + "\n");

	infoFile.close()
	print("File has been saved")

def readInput():
	inFile = open('info.txt', 'r')
	
	fileContents = inFile.read()

	inFile.close()

	print(fileContents)

def main():
	
	writeInput()

	print("\nContents in the text file: ");
	readInput()

main()