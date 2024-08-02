import tkinter as tk

# from datetime import datetime

# root window initialization
root = tk.Tk()
root.title("Quick Server Scanner")
root.geometry('720x700')

list_counter = 0


# Functions
def onclick():
    print("You clicked the button")


def getCounter() -> int:
    return list_counter


def incrementCounter(counter):
    counter += 1


def userPressedEnter(event):
    example.insert(0, txt.get())


# Main Body
# adding a label to the root window
lbl = tk.Label(root, text="Enter the SN for the Search List: ")
lbl.grid(column=0, row=0)

# adding Entry Field
txt = tk.Entry(root, width=80)
txt.bind('<Return>', userPressedEnter)
txt.grid(column=1, row=0)

# Set ListBox
example = tk.Listbox(root, width=100, height=30)
example.grid(column=0, row=1, columnspan=3)
example.insert(0, "")

# Execute Tkinter
root.mainloop()
