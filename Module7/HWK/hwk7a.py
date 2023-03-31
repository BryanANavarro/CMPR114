# Bryan Navarro
# CMPR114 - Python
# March 26, 2023
# Homework Assignment 7 - Project #1


str = input("Enter string: ")
vowels = 0
consonants = 0

for i in str:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels += 1
    elif( i == ' '):
        continue
    else:
        consonants += 1
 
print(f"Total Number of Vowels in this String = {vowels}")
print(f"Total Number of Consonants in this String = {consonants}")