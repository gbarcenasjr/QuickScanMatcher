import tkinter as tk

# Initialize GUI Window and Size
GUI = tk.Tk()
GUI.title("Quick Server Scanner")
GUI.geometry('720x700')


# Functions
def UserPressedEnter(event):
    example.insert(0, txt.get())
    txt.delete(0, 'end')
    txt.insert(0, "")


def ModeSwitch():
    my_text = mode_button['text']
    if my_text == "Switch To [SEARCH MODE]":
        entry_label.config(text="[SEARCH MODE] Enter the SN to search: ")
        mode_button.config(text="Switch To [LIST MODE]")
    elif my_text == "Switch To [LIST MODE]":
        entry_label.config(text="[LIST MODE] Enter the SN for the Search List: ")
        mode_button.config(text='"Switch To [SEARCH MODE]")


# ------------------- Main Body (Using Grid) -------------------
mode_button = tk.Button(GUI, text="Switch To [SEARCH MODE]", command=ModeSwitch)
mode_button.grid(column=0, row=0)

# Label for the Entry Field
entry_label = tk.Label(GUI, text="[LIST MODE] Enter the SN for the Search List: ")
entry_label.grid(column=0, row=1)

# Entry Field for user input
user_entry = tk.Entry(GUI, width=55)
user_entry.bind('<Return>', UserPressedEnter)
user_entry.grid(column=1, row=1, columnspan=2)

scroll_bar = tk.Scrollbar(GUI)
scroll_bar.grid(column=1, row=2, )
# Set ListBox
example = tk.Listbox(GUI, width=100, height=30, yscrollcommand=scroll_bar.set)
example.grid(column=0, row=2, columnspan=3)
# example.insert(0, example)


# Execute Tkinter
GUI.mainloop()
