# Bryan Navarro
# CMPR114 - Python
# March 6, 2023
# Quiz 1 - Project 4

commission = 0

sales = float(input("\nEnter sales amount: "))

if sales >= 50000 and sales < 70000:
	commission = 10
	print(f"Commission Rate: {commission}%")

elif sales >= 70000 and sales < 90000:
	commission = 20
	print(f"Commission Rate: {commission}%")

elif sales >= 90000 and sales < 110000:
	commission = 30
	print(f"Commission Rate: {commission}%")
else:
	print(f"Commission Rate: {commission}%")