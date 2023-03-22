# Bryan Navarro
# CMPR114 - Python
# March 20, 2023
# Challenge Exercise 5 - Project #5

import tkinter as tk # import the gui interface controls
from tkinter import messagebox # imports the messagebox display

win = tk.Tk() # create the window interface
win.geometry ("500x500") # width x height in pixels
win.title("Customer Information") #label for the title

lblLastname = tk.Label(win, text = "Enter the last name").grid(column = 0, row = 0) # label widget
lblFirstname = tk.Label(win, text = "Enter the first name").grid(column = 0, row = 1)
lblAddress = tk.Label(win, text = "Enter address").grid(column = 0, row = 2)
lblCity = tk.Label(win, text = "Enter city").grid(column = 0, row = 3)
lblState = tk.Label(win, text = "Enter state").grid(column = 0, row = 4)
lblZipCode = tk.Label(win, text = "Enter the zipcode").grid(column = 0, row = 5)

def write():
	textFile = open("Customer.txt", "a")
	content = textFile.write("Confirmation: " + str(LN.get() + ", " + FN.get() + "\n" + address.get() + "\n" + city.get() + "\n" + state.get() + "\n" + zipcode.get()))
	textFile.close()
	messagebox.showinfo("Information", "Data Recorded")

def quit():
	messagebox.showinfo("Information", "Thank you...")
	win.destroy() # closes the interface

def submit(): # function name
	messagebox.showinfo("Information", "Entered :" + LN.get() + "," + FN.get() + "\n" + address.get() + "\n" + city.get() + "\n" + state.get() + "\n" + zipcode.get()) # display info

LN = tk.StringVar() #the StringVar manages the Entry widget
txtLastName = tk.Entry(win, width = 12, textvariable = LN).grid(column = 1, row = 0) # Text Entry widget

FN = tk.StringVar()
txtFirstname = tk.Entry(win, width = 12, textvariable = FN).grid(column = 1, row = 1)

address = tk.StringVar()
txtAddress = tk.Entry(win, width = 12, textvariable = address).grid(column = 1, row = 2)

city = tk.StringVar()
txtCity = tk.Entry(win, width = 12, textvariable = city).grid(column = 1, row = 3)

state = tk.StringVar()
txtState = tk.Entry(win, width = 12, textvariable = state).grid(column = 1, row = 4)

zipcode = tk.StringVar()
txtZipCode = tk.Entry(win, width = 12, textvariable = zipcode).grid(column = 1, row = 5)


# commmand calls the click function
btnSubmit = tk.Button(win, text = "Submit", command = submit).grid(column = 0, row = 8) # button widget

# command calls the quit function
btnQuit = tk.Button(win, text = "Quit", command = quit).grid(column = 1, row = 8) # button widget

# command calls the write function
btnWrite = tk.Button(win, text = "Transfer", command = write).grid(column = 2, row = 8) # button widget

win.mainloop() #ensures the interfaces stays on the screen on window
submit()