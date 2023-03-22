# Bryan Navarro
# CMPR114 - Python
# March 22, 2023
# Homework Assignment 6 - Project #4

import tkinter as tk
from tkinter import messagebox

outfile = open("sumOfNumbers.txt", 'w')
for i in range(1, 11):
	outfile.write(f"{i * 100}\n")

outfile.close()
print("File has been created")



win = tk.Tk()
win.geometry("400x400")
win.title("Sum of Numbers")

def read():
	infile = open("sumOfNumbers.txt", 'r')
	line = infile.readline()
	sum = 0

	while line != '':
		sum += int(line)
		line = infile.readline()

	infile.close()
	messagebox.showinfo("Information", "The file has been read. The sum is " + str(sum))


def quit():
	messagebox.showinfo("Information", "Thank you...")
	win.destroy() # closes the interface



btnRead = tk.Button(win, text = "Read File", command = read).grid(column = 0, row = 2)

btnQuit = tk.Button(win, text = "Quit", command = quit).grid(column = 0, row = 3)

win.mainloop()
