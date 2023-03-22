# Bryan Navarro
# CMPR114 - Python
# March 20, 2023
# Challenge Exercise 5 - Project #2

def WriteNumbers():
	
	outfile = open('numbers.txt','a')

	num1 = int(input("\nEnter #1: "))
	num2 = int(input("\nEnter #2: "))
	num3 = int(input("\nEnter #3: "))

	sum = num1 + num2 + num3
	avg = sum/3

	outfile.write("\nThe 1st number is " + str(num1))
	outfile.write("\nThe 2nd number is " + str(num2))
	outfile.write("\nThe 3rd number is " + str(num3))
	outfile.write("\nThe average is " + str(avg))
	outfile.write("\nThe total number is " + str(sum))

	outfile.close()

	print ("\nData recorded.")

def ReadNumbers():

	infile = open('numbers.txt', 'r')

	content = infile.read()

	infile.close()
	
	print(content)


def main():

	WriteNumbers()
	ReadNumbers()

main()