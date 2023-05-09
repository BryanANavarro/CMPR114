# Bryan Navarro
# CMPR114 - Python
# May 8, 2023
# Class Exercise 11 - GUI Design Project #3

import tkinter

class MyGUI:
	def __init__(self):
		# Creat the main window widget
		self.main_window = tkinter.Tk()
	# Create a Label widget container the text "Hello World"
		self.label = tkinter.Label(self.main_window, text = "Hello World!")
		self.label2 = tkinter.Label(self.main_window, text = "Navarro")
		self.label3 = tkinter.Label(self.main_window, text = "Bryan")
		self.label4 = tkinter.Label(self.main_window, text = "28")

	# Call the Label widget's pack method.
		self.label.pack()
		self.label2.pack()
		self.label3.pack()
		self.label4.pack()

	# Enter the tkinter main loop.
		tkinter.mainloop()

# Create an instance of the MyGUI class
if __name__ == "__main__":
	my_gui = MyGUI()