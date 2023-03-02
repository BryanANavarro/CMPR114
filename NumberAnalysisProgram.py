# Bryan Navarro
# CMPR114 - Python
# March 1, 2023

numList = []
index = 0
total = 0
average = 0

while index < 5:
	# Get input from user
	num = int(input("\nEnter a number: "))

	# Append to numList
	numList.append(num)

	total += num
	# Increment the index
	index += 1
	# set highest and lowest to the first element of the list
	if len(numList) == 1:
		highest = numList[0]
		lowest = numList[0]
	else:
		if num > highest:
			highest = num
		if num < lowest:
			lowest = num	

average = total/len(numList)

print(f"\nLowest: {lowest}")
print(f"\nHighest: {highest}")
print(f"\nTotal: {total}")
print(f"\nAverage: {average}")
