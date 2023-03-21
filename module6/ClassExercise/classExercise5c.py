# Bryan Navarro
# CMPR114 - Python
# March 20, 2023
# Challenge Exercise 5 - Project #3

def sales():
	
	salary = float(input("\nEnter salary: "))
	num_days = int(input("\nEnter the days of sales: "))
	sales_file = open('sales.txt', 'a')
	sum = 0.0
	for count in range(1, num_days + 1):

		sales = float(input("Enter the sales for day # " + str(count) + " : "))
		sales_file.write(str(sales) + '\n')
		sum += sales

	
	if sum > 1000:
			salary = salary + (salary* .10)
			sales_file.write(str(salary) + '\n')
	sales_file.close()
	print("\nSales recorded.")
sales()

def ReadSales():

	sales_file = open('sales.txt', 'r')
	line = sales_file.readline()

	while line != '': 
		amount = float(line)

		print(f"{amount:.2f}")
		line = sales_file.readline()
	sales_file.close()
ReadSales()
