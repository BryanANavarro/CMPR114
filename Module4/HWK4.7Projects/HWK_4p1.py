# Bryan Navarro
# CMPR114 - Python
# March 7, 2023
# HWK_4.7 - Project 1

test_tup = (15, 20, 123, 47, 26, 81)
i = 0
total = 0
while i < len(test_tup):
	print(test_tup[i])
	total += test_tup[i]
	i = i + 1
print(f"\nTotal: {total}")

