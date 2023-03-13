# Bryan Navarro
# CMPR114 - Python
# March 6, 2023
# Quiz 1 - Project 5

commission = 0.0
total = 0.0
sales = float(input("\nEnter sales amount: "))

if sales >= 50000 and sales < 70000:
	commission = 10.0
	salary = 70000.00
	total = salary + (salary * commission/100)
	print(f"Commission Rate: {commission}%")
	print(f"Salary: ${salary:,.2f}")
	print(f"Total: ${total:,.2f}")
elif sales >= 70000 and sales < 90000:
	commission = 20.0
	salary = 80000.00
	total = salary + (salary * commission/100)
	print(f"Commission Rate: {commission}%")
	print(f"Salary: ${salary:,.2f}")
	print(f"Total: ${total:,.2f}")
elif sales >= 90000 and sales < 110000:
	commission = 30.0
	salary = 90000.00
	total = salary + (salary * commission/100)
	print(f"Commission Rate: {commission}%")
	print(f"Salary: ${salary:,.2f}")
	print(f"Total: ${total:,.2f}")
else:
	commission = 0.0
	salary = 50000.00
	total = salary + (salary * commission/100)
	print(f"Commission Rate: {commission}")
	print(f"Salary: ${salary:,.2f}")
	print(f"Total: ${total:,.2f}")