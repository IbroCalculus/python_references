import tkinter as tk
from tkinter import ttk

root = tk.Tk()

pic = tk.PhotoImage(file='Images/picture.png')

selection = tk.StringVar()
selection.set('Tuesday')

dropdown = tk.OptionMenu(root, selection, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
dropdown.pack()


options = [
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",]

selection1 = tk.StringVar()
selection1.set('PICK ANY NUMBER')

dropdown1 = ttk.OptionMenu(root, selection1, *options)
dropdown1.pack()

def check():
    label['text'] = selection.get()

def check1():
    label['text'] = selection1.get()


btn = tk.Button(root, text='CHECK SELECTION', command=check)
btn.pack()

btn1 = tk.Button(root, text='CHECK SELECTION', command=check1)
btn1.pack()


label = tk.Label(root, text='Awaiting Selection')
label.pack()

print(dropdown.keys())

root.mainloop()
