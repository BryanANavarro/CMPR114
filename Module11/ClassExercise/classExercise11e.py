# Bryan Navarro
# CMPR114 - Python
# May 8, 2023
# Class Exercise 11 - GUI Design Project #5

import tkinter
class MyGUI:
	def __init__(self):
		# Create the main window
		self.main_window = tkinter.Tk()

		# Create the two labels widegets
		self.label1 = tkinter.Label(self.main_window, text = "Hello World!")
		self.label2 = tkinter.Label(self.main_window, text = "This is my GUI program")

		# Call bot Label widegets' pack method.
		self.label1.pack(side = "left")
		self.label2.pack(side = "left")

		# Enter the tkinter main LookupErrortkinter.mainloop()
		tkinter.mainloop()

# Create an instance of the MyGUI class
if __name__ == "__main__":
	my_gui = MyGUI()