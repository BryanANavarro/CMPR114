# Bryan Navarro
# CMPR114 - Python
# April 24, 2023
# Class Exercise 10 - Inheritance class Project #4-2

import classExercise10d1

def main():
	used_car = classExercise10d1.Automobiles("Audi", 2022, 45000, 80000.0, 4)

	used_car2 = classExercise10d1.Automobiles("Honda", 2022, 45000, 80000.0, 4)

	print(f"Make: {used_car.get_make()}")
	print(f"Model: {used_car.get_model()}")
	print(f"Mileage: {used_car.get_mileage()}")
	print(f"Price: {used_car.get_price()}")
	print(f"Doors: {used_car.get_doors()}")

	print(f"\nMake: {used_car2.get_make()}")
	print(f"Model: {used_car2.get_model()}")
	print(f"Mileage: {used_car2.get_mileage()}")
	print(f"Price: {used_car2.get_price()}")
	print(f"Doors: {used_car2.get_doors()}")

main()