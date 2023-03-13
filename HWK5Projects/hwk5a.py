# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Homework Assignment 5 - Project #1

def main():
	price = float(input("\nEnter the price for the property: "))

	displayAssessment(price)

def displayAssessment(value):
	
	assessmentValue = value * 0.60
	propertyTax = (assessmentValue/100) * 0.72

	print(f"\nAssessment value is: ${assessmentValue:,.2f}.")
	print(f"\nProperty Tax: ${propertyTax:,.2f}. ")

main()