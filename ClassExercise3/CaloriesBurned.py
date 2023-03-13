# Bryan Navarro
# CMPR114 - Python
# February 27, 2023

caloriesPerMin = 4.2

for minutes in [10,15,20,25,30]:
	caloriesBurned = caloriesPerMin * minutes
	print(f"Total calories burned at {minutes} minutes: {caloriesBurned} calories")