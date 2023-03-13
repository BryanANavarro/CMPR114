# Bryan Navarro
# CMPR114 - Python
# February 13, 2023

guests = int(input("\nEnter the number of guests: "))
hot_Dogs = int(input("\nEnter how many hot dogs each guest is going to eat: "))

total = guests * hot_Dogs
buns = 8
dogs = 10

buns_Packages = round(total/buns)
dogs_Packages = round(total/dogs)

leftOver_Buns = (buns_Packages * buns) - total
leftOver_Dogs = (dogs_Packages * dogs) - total

print("\nThe minimum number of packages of hot dogs required is : " + str(dogs_Packages))
print("\nThe minimum number of packages of buns required is : " + str(buns_Packages))
print("\nThe number of hot dogs that will be left over is : " + str(leftOver_Dogs))
print("\nThe number of buns that will be left over is : " + str(leftOver_Buns))

