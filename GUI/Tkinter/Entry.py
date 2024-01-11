import tkinter as tk
from tkinter import ttk

root = tk.Tk()

entry_1 = tk.Entry(root, width=50)
entry_1.pack()

spacer = tk.Label(root, text="", height=1)
spacer.pack()

entry_1 = ttk.Entry(root, width=50)
entry_1.pack()

def y():
    print(entry_1.get())

button = ttk.Button(root, text="Click here", command=y)
button.pack()


root.mainloop()
