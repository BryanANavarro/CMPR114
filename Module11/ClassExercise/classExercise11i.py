# Bryan Navarro
# CMPR114 - Python
# May 8, 2023
# Class Exercise 11 - GUI Design Project #9

import tkinter
import tkinter.messagebox

class MyGUI:
	def __init__(self):
		# Create the main window widget.
		self.main_window = tkinter.Tk()

		# Create a Button widget. The text "Click ME!"
		# should appear on the face of the Button. The 
		# do_something method should be executed when 
		# the user clicks the Button.
		self.my_button = tkinter.Button(self.main_window, text = "Click Me!", command=self.do_something)

		# Pack the button.
		self.my_button.pack()

		# Enter hte tkinter main loop
		tkinter.mainloop()

	# The do_somethign method is a callback function
	# for the Button widget

	def do_something(self):
		# Display an info dialog box.
		tkinter.messagebox.showinfo("Response", "Thanks for clicking the button.")

# Create an instance of the MyGUI class
if __name__ == "__main__":
	my_gui = MyGUI()