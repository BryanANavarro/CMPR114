# Bryan Navarro
# CMPR114 - Python
# February 13, 2023

month = int(input("\nEnter the number of a month between 1 - 12: "))

if month >=1 and month <= 3:
	print("\nThe month is in the first quarter")
elif month >= 4 and month <= 6:
	print ("\nThe month is in the second quarter")
elif month >= 7 and month <= 9:
	print ("\nThe month is in the second quarter")
elif month >= 10 and month <= 12:
	print ("\nThe month is in the second quarter")
else:
	print("\nERROR. ENter a value between 1 - 12.")