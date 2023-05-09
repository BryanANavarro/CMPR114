# Bryan Navarro
# CMPR114 - Python
# May 8, 2023
# Class Exercise 11 - GUI Design Project #2

import tkinter

class MyGUI:

	def __init__(self):

	# Creat the main window widget.
		self.main_window = tkinter.Tk()

	# Display a title.
		self.main_window.title("My First GUI")
		self.main_window.geometry("400x100")

	# Enter the tkinter main loop
		tkinter.mainloop()

if __name__ == "__main__":
	my_gui = MyGUI()

