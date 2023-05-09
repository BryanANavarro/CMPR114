# Bryan Navarro
# CMPR114 - Python
# May 8, 2023
# Class Exercise 11 - GUI Design Project #10

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


		# Create a Qui button. When this button is clicked
		# the root widget's destroy method  is called.
		# (The main_window variable references the root widget,
		# so the callback function is self.main_window.destory.)
		self.quit_button = tkinter.Button(self.main_window, text = "Quit", command = self.main_window.destroy)

		self.good_button = tkinter.Button(self.main_window, text = "Quote", command = self.quote)

		# Pack the button.
		self.my_button.pack()
		self.quit_button.pack()
		self.good_button.pack()

		# Enter hte tkinter main loop
		tkinter.mainloop()

	# The do_somethign method is a callback function
	# for the Button widget

	def do_something(self):
		# Display an info dialog box.
		tkinter.messagebox.showinfo("Response", "Thanks for clicking the button.")
	
	def quote(self):
		tkinter.messagebox.showinfo("Response", "You are awesome!")

# Create an instance of the MyGUI class
if __name__ == "__main__":
	my_gui = MyGUI()