from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(number.get())
        result.set(value * value)
    except ValueError:
        pass

root = Tk() #Create main application window
root.title("Calculator")

# Create a Frame widget
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #Place frame inside main application window
root.columnconfigure(0, weight=1) #Expand frame if window is resized
root.rowconfigure(0, weight=1)

# Entry Widget
number = StringVar()
number_entry = ttk.Entry(mainframe, width=7, textvariable=number)
number_entry.grid(column=2, row=1, sticky=(W,E))

# Result widget
result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W,E))

# Calculate Button
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# Add padding to all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Put focus on entry 
number_entry.focus()

root.bind("<Return>", calculate)

# Start the event loop
root.mainloop()


