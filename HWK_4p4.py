# Bryan Navarro
# CMPR114 - Python
# March 7, 2023
# HWK_4.7 - Project 4

input_tup = ([2, 20], [44,1], [3,13])
print("\nUnsorted")
print(input_tup)

print("\nSorted by Summation")

sort_tup= sorted(input_tup, key = lambda x:x[0] + x[1])
print(sort_tup)