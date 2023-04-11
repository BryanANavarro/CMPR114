# Bryan Navarro
# CMPR114 - Python
# April 10, 2023
# Midterm Project #1

def main():
	fats = float(input("\nEnter the grams of fat: "))
	carbs = float(input("\nEnter the grams of carbs: "))

	print(f"The number of calories in fats is: {calcFats(fats)}")
	print(f"The number of calories in fats is: {calcCarbs(carbs)}")

def calcFats(fats):
	calories = fats * 9

	return calories

def calcCarbs(carbs):
	calories = carbs * 4

	return calories

main()