# Bryan Navarro
# CMPR114 - Python
# April 17, 2023
# Homework Assignment 7 - Project #2b

import EmployeeClass

def main():
	Employee1 = EmployeeClass.Employee("Susan Meyers", "47899", "Accounting", "Vice President")
	Employee2 = EmployeeClass.Employee("Mark Jones", "39119", "IT", "Programmer")
	Employee3 = EmployeeClass.Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

	print(f"\nThe name of Employee 1 is {Employee1.get_name()}, ID: {Employee1.get_ID()}, Department: {Employee1.get_department()}, Title: {Employee1.get_title()}")
	print(f"\nThe name of Employee 2 is {Employee2.get_name()}, ID: {Employee2.get_ID()}, Department: {Employee2.get_department()}, Title: {Employee2.get_title()}")
	print(f"\nThe name of Employee 3 is {Employee3.get_name()}, ID: {Employee3.get_ID()}, Department: {Employee3.get_department()}, Title: {Employee3.get_title()}")

main()
