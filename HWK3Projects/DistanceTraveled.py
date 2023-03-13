# Bryan Navarro
# CMPR114 - Python
# March 1, 2023

# Get input from the user
speed = int(input("\nWhat is the speed of the vehicle in mph? "))
hours = int(input("\nHow many hours has it traveled? "))

print("\nHours		Distance Traveled")

for i in range(hours):
	# For every hour starting at 1, multiply it by the distance traveled
	distance = speed * (i+1)
	# Display Results
	print(f"\n{i+1}			{distance}")