# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Homework Assignment 5 - Project #3

STATE_TAX = 0.05
COUNTY_TAX = 0.025

def main():
	sales = float(input("\nEnter the total sales for the month: "))

	calculateTaxes(sales)

def calculateTaxes(sales):
	
	countyTaxAmount = sales * COUNTY_TAX
	stateTaxAmount = sales * STATE_TAX

	totalSalesTax = countyTaxAmount + stateTaxAmount

	print(f"\nCounty sales tax: ${countyTaxAmount:,.2f}")
	print(f"State sales tax: ${stateTaxAmount:,.2f}")
	print(f"Total sales tax: ${totalSalesTax:,.2f}")


main()