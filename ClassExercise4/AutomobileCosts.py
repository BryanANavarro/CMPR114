# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Challenge Exercise 4 - Part 2: Project #2

def main():
	
	monthlyCosts()


def monthlyCosts():
	loanPayment = float(input("\nEnter loan payment: "))
	insurance = float(input("Enter insurance payment: "))
	gas = float(input("Enter gas payment: "))
	oil = float(input("Enter oil payment: "))
	tires = float(input("Enter tire amount: "))
	maintenance = float(input("Enter maintenance amount: "))
	
	displayMonthlyCost(loanPayment, insurance, gas, oil, tires, maintenance)

def displayMonthlyCost(loan, insurance, gas, oil, tires, maintenance):
	print("\nMontly Costs:")
	print(f"Loan amount: ${loan:.2f}")
	print(f"Insurance amount: ${insurance:.2f}")
	print(f"Gas amount: ${gas:.2f}")
	print(f"Oil amount: ${oil:.2f}")
	print(f"Tires amount: ${tires:.2f}")
	print(f"Maintenance amount: ${maintenance:.2f}")

	displayYearlyCost(loan, insurance, gas, oil, tires, maintenance)

def displayYearlyCost(loan, insurance, gas, oil, tires, maintenance):
	
	yearlyLoan = loan * 12
	yearlyIns = insurance * 12
	yearlyGas = gas * 12
	yearlyOil = oil * 12
	yearlyTires = tires * 12
	yearlyMaintenance = maintenance * 12

	print("\nYearly Costs: ")
	print(f"Loan amount: ${yearlyLoan:.2f}")
	print(f"Insurance amount: ${yearlyIns:.2f}")
	print(f"Gas amount: ${yearlyGas:.2f}")
	print(f"Oil amount: ${yearlyOil:.2f}")
	print(f"Tires amount: ${yearlyTires:.2f}")
	print(f"Maintenance amount: ${yearlyMaintenance:.2f}")

main()