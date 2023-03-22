# Bryan Navarro
# CMPR114 - Python
# March 20, 2023
# Challenge Exercise 5 - Project #8

import random

randomList = []
outfile = open("randomList.txt", 'w')

for i in range(0, 10):
	randomList.append(random.randint(0, 10))
	

outfile.write("\n" + str(randomList))

outfile.close()
print("\nData Recorded")

infile = open("randomList.txt", 'r')

content = infile.read()
infile.close()
print(content)
