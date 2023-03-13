# Bryan Navarro
# CMPR114 - Python
# February 27, 2023

flag = 'y'
totalCommission = 0.0
totalSales = 0.0

while flag == 'y':
	sales = float(input("\nEnter the amount of sales: "))
	commRate = float(input("\nEnter the commission rate: "))
	commission = sales * (commRate/100)
	totalCommission +=commission
	totalSales += sales
	flag = input("\nDo you want to add another sales and commission value? y-yes or n-no ")


print("The sales amount: ${:.2f}".format(totalSales))
print("The commission amount: ${:.2f}".format(totalCommission))