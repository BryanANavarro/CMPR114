# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Homework Assignment 7 - Project #2

string = input("Enter string: ").upper()

count = 0
totalCount = 0
mostFrequentCh = ""

for ch in string:
	for str1 in string:
		if str1 == ch:
			count += 1
	if count > totalCount:
		totalCount = count
	count = 0

for ch in string:
	for str1 in string:
		if str1 == ch:
			count += 1
	if count == totalCount:
		if (ch not in mostFrequentCh): 
			mostFrequentCh += ch
	count = 0

print(f"The most frequent character is {mostFrequentCh} and appears {totalCount} times.")