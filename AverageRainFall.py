# Bryan Navarro
# CMPR114 - Python
# March 1, 2023


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainFall = []
numberOfYears = int(input("\nEnter the amount of years to calculate: "))


for i in range(1, numberOfYears+1):
	for j in months:
		rain = float(input(f"\nEnter the amount of rain for {j} in year {i}: "))
		rainFall.append(rain)
	totalMonths = numberOfYears * 12
	totalRain = sum(rainFall)
	averageRain = totalRain/len(rainFall)

print(f"\nTotal number of months calculated: {totalMonths} months.")
print(f"The total rain in the entire time period was: {totalRain:.2f} inches.")
print(f"The average rainfall is: {averageRain:.2f} inches.\n")