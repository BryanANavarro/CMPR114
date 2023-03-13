# Bryan Navarro
# CMPR114 - Python
# February 27, 2023

DAYS = 5
total = 0

for counter in range(DAYS):
	bugs = int(input("\nEnter how many bugs were collected: "))
	total += bugs

print(f"\nTotal amount of bugs collected: {total}")