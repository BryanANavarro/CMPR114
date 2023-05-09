# Bryan Navarro
# CMPR114 - Python
# May 8, 2023
# Class Exercise 11 - GUI Design Project #7

import tkinter
class MyGUI:
	def __init__(self):
		# Create the main window
		self.main_window = tkinter.Tk()

		# Create the two labels widegets
		self.label1 = tkinter.Label(self.main_window, text = "Hello World!", borderwidth=1, relief="solid")
		self.label2 = tkinter.Label(self.main_window, text = "This is my GUI program.", borderwidth=1, relief="solid")
		
		self.label1.pack(padx=20, pady=20)
		self.label2.pack(padx=20, pady=20)

		# enter the tkinter main loop
		tkinter.mainloop()

# Create an instance of MyGUI class
if __name__ == "__main__":
	my_gui = MyGUI()