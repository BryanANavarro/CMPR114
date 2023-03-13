# Bryan Navarro
# CMPR114 - Python
# March 1, 2023

# The get_scores function gets a series of test
# scores from the user and stores them in a list.
# A reference to the list is returned.

def main():
	
	# Get the test scores form the user.
	scores = getScores()

	#Get the total of the test scores.
	total = getTotal(scores)

	# Get the lowest test score.
	lowest = min(scores)

	# Subtract the lowest score from the total.
	total -= lowest

	# Calculate the average. Note that we divide by 1 less than the number
	# of scores because the lowest score was dropped
	average = total/ (len(scores) - 1)

	# Display the average
	print(f"Average with lowest score dropped: {average}")

def getScores():
	
	# Create an emtpy list.
	testScores = []

	# Create a variable to control the loop.
	again = 'y'

	# Get the scores form the user and add them to the list.
	while again == 'y':
		
		# Get a score and add it to the list.
		value = float(input("\nEnter a test score: "))
		testScores.append(value)

		# Want to do this again?
		print("\nDo you want to add another score?")
		again = input("y = yes, anything else = no: ")
		print()
	
		# Return the list.
	return testScores

# The getTotal function accepts a list as an argument
# returns the total of the values in the list

def getTotal(valueList):
	# Create a variable to use as an accumulator.
	total = 0.0

	# Caluculate the total of the list elements. 
	for num in valueList:
		total += num
		
	# Return the total.
	return total

# Call the main funciton.
if __name__ == '__main__':
	main()