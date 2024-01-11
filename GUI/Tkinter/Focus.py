import tkinter as tk
from tkinter import ttk


root = tk.Tk()

label_1 = tk.Label(root, text="This is Label 1", font="Times 24", bg="red")
label_1.pack()


entry = tk.Entry(root, width=50)
entry.pack()

label_2 = tk.Label(root, text="This is Label 2", font="Times 24", bg="blue")
label_2.pack()

entry1 = tk.Entry(root, width=50)
entry1.pack()

entry1.focus()

#Pressing tab changes the focus


root.mainloop()
