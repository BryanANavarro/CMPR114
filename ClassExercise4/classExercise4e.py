# Bryan Navarro
# CMPR114 - Python
# March 13, 2023
# Challenge Exercise 4 - Part 1: Project #5


def main():
	hours = float(input("\nEnter the hours worked: "))
	rate = float(input("\nEnter the hourly rate: "))

	# calling the two functions
	show_hours(hours)
	show_rate(rate)


def show_hours(hours):
	print(f"\nHours: {hours}.")


def show_rate(rate):
	print(f"\nRate: ${rate:.2f} per hour.")

# Call the main function
main()