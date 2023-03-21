# Bryan Navarro
# CMPR114 - Python
# March 20, 2023
# Challenge Exercise 5 - Project #6

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("300x300")
win.title("Numbers List")

lblfirstNumber = tk.Label(win, text = "Enter first number").grid(column = 0, row = 0) 
lblsecondNumber = tk.Label(win, text = "Enter second number").grid(column = 0, row = 1)
lblthirdNumber = tk.Label(win, text = "Enter third number").grid(column = 0, row = 2) 

def write():
	textFile = open("NumbersGUI.txt", "w")
	content = textFile.write("Numbers list: \n" + str(FN.get() + ", " + SN.get() + " and " + TN.get()))
	textFile.close()
	messagebox.showinfo("Information", "Data Recorded")

def quit():
	messagebox.showinfo("Information", "Thank you...")
	win.destroy() # closes the interface

def submit(): # function name
	messagebox.showinfo("Information", "Entered :" + FN.get() + ", " + SN.get() + " and " + TN.get()) # display info

FN = tk.StringVar() #the StringVar manages the Entry widget
txtFirstNumber = tk.Entry(win, width = 12, textvariable = FN).grid(column = 1, row = 0) # Text Entry widget

SN = tk.StringVar()
txtSecondNumber = tk.Entry(win, width = 12, textvariable = SN).grid(column = 1, row = 1)

TN = tk.StringVar()
txtThirdNumber = tk.Entry(win, width = 12, textvariable = TN).grid(column = 1, row = 2)

# commmand calls the click function
btnSubmit = tk.Button(win, text = "Submit", command = submit).grid(column = 0, row = 4) # button widget

# command calls the quit function
btnQuit = tk.Button(win, text = "Quit", command = quit).grid(column = 1, row = 4) # button widget

# command calls the write function
btnWrite = tk.Button(win, text = "Transfer", command = write).grid(column = 2, row = 4) # button widget

win.mainloop() #ensures the interfaces stays on the screen on window
submit()