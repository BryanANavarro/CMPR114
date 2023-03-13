# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Homework Assignment 5 - Project #2

def main():

	seatA = int(input("\nEnter how many class A seats were sold: "))
	seatB = int(input("\nEnter how many class B seats were sold: "))
	seatC = int(input("\nEnter how many class C seats were sold: "))

	calculateAmount(seatA, seatB, seatC)

def calculateAmount(a, b, c):
	seatA = a * 20.00
	seatB = b * 15.00
	seatC = c * 10.00

	total = seatA + seatB + seatC

	print(f"\nIncome from class A seats: ${seatA:,.2f}.")
	print(f"Income from class B seats: ${seatB:,.2f}.")
	print(f"Income from class C seats: ${seatC:,.2f}.")
	print(f"\nTotal Income: ${total:,.2f}.")

main()