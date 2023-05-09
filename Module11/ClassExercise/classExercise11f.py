# Bryan Navarro
# CMPR114 - Python
# May 8, 2023
# Class Exercise 11 - GUI Design Project #6

import tkinter
class MyGUI:
	def __init__(self):
		# Create the main window
		self.main_window = tkinter.Tk()

		# Create the two labels widegets
		self.label1 = tkinter.Label(self.main_window, text = "Hello World!", borderwidth=1, relief="solid")
		self.label2 = tkinter.Label(self.main_window, text = "This is my GUI program.", borderwidth=1, relief="solid")
		self.label3 = tkinter.Label(self.main_window, text = "I'm still learning!", borderwidth=1, relief="solid")
		self.label4 = tkinter.Label(self.main_window, text = "This is a good start!", borderwidth=1, relief="solid")


		self.label1.pack(ipadx=20, ipady=20)
		self.label2.pack(ipadx=20, ipady=20)
		self.label3.pack(ipadx=20, ipady=20)
		self.label4.pack(ipadx=20, ipady=20)

		# enter the tkinter main loop
		tkinter.mainloop()

# Create an instance of MyGUI class
if __name__ == "__main__":
	my_gui = MyGUI()