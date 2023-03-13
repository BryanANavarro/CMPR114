# Bryan Navarro
# CMPR114 - Python
# March 6, 2023
# Quiz 1 - Project 6

scores = []
for i in range(1,5):
	score = int (input(f"\nEnter score {i}: "))
	scores.append(score)

total = sum(scores)
average = total/4

while average > 0 :
	if average > 100:
		print("\nAverage is above 100. Enter test scores again.")
		break
	elif average >= 90 and average <= 100:
		print("\nGrade: A")
		print(f"Total: {total}")
		print(f"Average: {average}")
		break
	elif average >= 80 and average < 90:
		print("\nGrade: B")
		print(f"Total: {total}")
		print(f"Average: {average}")
		break
	elif average >= 70 and average < 80:
		print("\nGrade: C")
		print(f"Total: {total}")
		print(f"Average: {average}")
		break
	elif average >= 60 and average < 70:
		print("\nGrade: D")
		print(f"Total: {total}")
		print(f"Average: {average}")
		break
	elif average < 60:
		print("\nGrade: F")
		print(f"Total: {total}")
		print(f"Average: {average}")
		break
	else:
		print("\nEnter the numbers again")
		break