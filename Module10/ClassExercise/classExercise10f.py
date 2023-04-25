# Bryan Navarro
# CMPR114 - Python
# April 24, 2023
# Class Exercise 10 - Inheritance class Project #6

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

	truck = classExercise10d1.Automobiles("Toyota", "Tacoma", 40000, 12000.0, 4)
	suv = classExercise10d1.Automobiles("Volvo", "SE", 30000, 18500.0, 4)
	electric = classExercise10d1.Automobiles("Tesla", "Model Y", 1000, 65000, 4)

	print(f"\nMake: {truck.get_make()}")
	print(f"Model: {truck.get_model()}")
	print(f"Mileage: {truck.get_mileage()}")
	print(f"Price: {truck.get_price()}")
	print(f"Doors: {truck.get_doors()}")

	print(f"\nMake: {suv.get_make()}")
	print(f"Model: {suv.get_model()}")
	print(f"Mileage: {suv.get_mileage()}")
	print(f"Price: {suv.get_price()}")
	print(f"Doors: {suv.get_doors()}")

	print(f"\nMake: {electric.get_make()}")
	print(f"Model: {electric.get_model()}")
	print(f"Mileage: {electric.get_mileage()}")
	print(f"Price: {electric.get_price()}")
	print(f"Doors: {electric.get_doors()}")
main()