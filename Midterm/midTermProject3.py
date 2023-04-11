# Bryan Navarro
# CMPR114 - Python
# April 10, 2023
# Midterm Project #3

outfile = open("Coffee.txt", 'a')

brand = input("\nEnter your favorite coffee brand: ")

outfile.write(f"\n{brand},99-8888,9.88")

outfile.close()

infile = open("Coffee.txt", 'r')

content = infile.read()

infile.close()

print(content)