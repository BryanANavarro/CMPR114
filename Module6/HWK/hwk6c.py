# Bryan Navarro
# CMPR114 - Python
# March 22, 2023
# Homework Assignment 6 - Project #3

outfile = open("number_list.txt", 'w')

for i in range(1, 101):
	outfile.write(f"Number: {i}\n")
outfile.close()

print("number_list.txt has been created")