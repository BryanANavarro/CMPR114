# Bryan Navarro
# CMPR114 - Python
# March 6, 2023
# Quiz 1 - Project 2

numList = []
index = 0
sum = 0
average = 0

while index < 4:
	num = int(input("\nEnter score: "))

	numList.append(num)

	sum+=num
	index+=1
average = sum/len(numList)

print(f"\nSum: {sum}")
print(f"\nAverage: {average}")