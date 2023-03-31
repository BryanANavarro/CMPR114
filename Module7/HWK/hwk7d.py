# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Homework Assignment 7 - Project #4

string = input("English: ")

pigLatin = ""

for word in string.split(" "):
	pigLatin = pigLatin + (word[1:] + word[0] + "ay").upper() + " ";

print(f"Pig Lating: {pigLatin}")