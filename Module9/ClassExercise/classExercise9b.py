# Bryan Navarro
# CMPR114 - Python
# April 17, 2023
# Class Exercise 9 - Object Oriented Programming + Class - Project #2

class Teacher:
	#using init to create a customized constructor
	#here we have three arguments
	def __init__(self, name, classRoom, course):
		self.name = name
		self.classRoom = classRoom
		self.course = course
	def GetProfessor(self):
		print("\nProfessor Name is " + self.name)
		print("Professor assigned class is " + self.classRoom)
		print("Professor is teaching " + self.course)

Teacher1 = Teacher("Prof. Sim", "A206", "Python Programming" )
Teacher1.GetProfessor()

Teacher2 = Teacher("Prof. Navarro", "A208", "Java Programming")
Teacher2.GetProfessor()