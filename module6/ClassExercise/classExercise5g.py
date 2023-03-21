# Bryan Navarro
# CMPR114 - Python
# March 20, 2023
# Challenge Exercise 5 - Project #7

midterm = float(input("\nEnter midterm score: "))
final = float(input("\nEnter final score: "))
average = (midterm + final)/2

gradeFile = open("Grades.txt", 'a')

while average > 0 :
	if average > 100:
		print("\nAverage is above 100. Enter test scores again.")
		break
	elif average >= 90 and average <= 100:
		gradeFile.write("\nAverage grade: " + str(average))
		gradeFile.write("\nLetter grade: A\n")
		break
	elif average >= 80 and average < 90:
		gradeFile.write("\nAverage grade: " + str(average))
		gradeFile.write("\nLetter grade: B\n")
		break
	elif average >= 70 and average < 80:
		gradeFile.write("\nAverage grade: " + str(average))
		gradeFile.write("\nLetter grade: C\n")
		break
	elif average >= 60 and average < 70:
		gradeFile.write("\nAverage grade: " + str(average))
		gradeFile.write("\nLetter grade: D\n")
		break
	elif average < 60:
		gradeFile.write("\nAverage grade: " + str(average))
		gradeFile.write("\nLetter grade: F\n")
		break
	else:
		print("\nEnter the numbers again")
		break

gradeFile.close()
print("\nData Recorded.")

readFile = open("Grades.txt", 'r')

content = readFile.read()
readFile.close()

try:
	print(content)
except:
	print("\nSomething went wrong")
