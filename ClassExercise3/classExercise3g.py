# Bryan Navarro
# CMPR114 - Python
# February 27, 2023

product = 0.0

while product < 100:
	number = float(input("\nEnter a number: "))
	product = number * 10
	if product >= 100:
		print(f"\nThe product is {product}. It hit 100 so the program will end.")
