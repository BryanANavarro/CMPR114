# Bryan Navarro
# CMPR114 - Python
# March 20, 2023
# Challenge Exercise 5 - Project #4

def main():
	num_emps = int(input("\nEnter the number of employee records: "))

	emp_file = open('employees.txt', 'w')

	for count in range(1, num_emps + 1):
		print("\nEnter data for employee #", count)

		name = input("\nName: ")
		id_num = input("ID Number: ")
		dept = input("Department: ")

		emp_file.write("Name:" + name + '\n')
		emp_file.write("ID:" + id_num + '\n')
		emp_file.write("Department:" + dept + "\n\n")

		print()

	emp_file.close()
	print("\nData Recorded.")

	readFile = open('employees.txt', 'r')

	content = readFile.read()

	readFile.close()

	print(content)
main()