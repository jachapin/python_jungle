from tkinter import *
from tkinter import ttk

root = Tk() #Create main application window
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #Place frame inside main application window
root.columnconfigure(0, weight=1) #Expand frame if window is resized
root.rowconfigure(0, weight=1)

number = StringVar()
number_entry = ttk.