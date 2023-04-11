# Bryan Navarro
# CMPR114 - Python
# April 10, 2023
# Midterm Project #4

rent = float(input("\nEnter your rent expense: "))
gas = float(input("\nEnter your gas expense: "))
food = float(input("\nEnter your food expense: "))
clothing = float(input("\nEnter your clothing expense: "))
car = float(input("\nEnter your car expense: "))

outfile = open("expense.txt", 'w')

outfile.write(f"Rent: {rent}\nGas: {gas}\nFood: {food}\nClothing: {clothing}\nCar: {car}")

outfile.close()

infile = open("expense.txt", 'r')

content = infile.read()

infile.close()

print(content)