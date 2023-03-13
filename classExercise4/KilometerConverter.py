# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Challenge Exercise 4 - Part 2: Project #1

def main():
	distance = float(input("\nEnter the distance traveled in kilometers: "))

	print(f"\nKilometers: {distance} kilometers.")
	print(f"\nMiles: " + str(convertToMiles(distance)) + " miles." )

# convertToMiles function accepts kilometers as an argument
def convertToMiles(kilometers):
	miles = kilometers * 0.6214
	return miles

main()