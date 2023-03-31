# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Homework Assignment 7 - Project #5

def encryptStr(string, shift):
	encryptedString = ""

	for ch in string:
		if ch == " ":
			encryptedString=encryptedString + ch
		elif(ch.isupper()):
			encryptedString = encryptedString + chr((ord(ch) + shift - 65) % 26 + 65)
		else:
			encryptedString = encryptedString + chr((ord(ch) + shift - 97) % 26 + 97)

	return encryptedString

string = input("Enter string: ")
shift = int(input("Enter amount to shift by: "))

print(encryptStr(string, shift))