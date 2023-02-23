# Bryan Navarro
# CMPR114 - Python
# February 13, 2023

price = 99
packages = int(input("\nEnter the number of packages purchased: "))

if packages >= 10 and packages <= 19:
	discount = 10
	print("\nThe discount is: " + str(discount) + "%")
elif packages >= 20 and packages <= 49:
	discount = 20
	print("\nThe discount is: " + str(discount) + "%")
elif packages >= 50 and packages <= 99:
	discount = 30
	print("\nThe discount is: " + str(discount) + "%")
elif packages >= 100:
	discount = 40
	print("\nThe discount is: " + str(discount) + "%")
else:
	discount = 0
	print("\nThe discount is: " + str(discount) + "%")

totalNoDiscount = packages * price
total = totalNoDiscount -  (totalNoDiscount * (discount/100))

print("\nThe total with the disocunt is: ${:.2f}".format(total))