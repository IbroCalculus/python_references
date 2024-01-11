import tkinter as tk
from tkinter import ttk


root = tk.Tk()

spin = tk.Spinbox(root, from_=1, to=10)
spin.pack()

label = tk.Label(root, text="", pady=2)
label.pack()

spin1 = ttk.Spinbox(root, from_=1, to=10)
spin1.pack()



root.mainloop()
