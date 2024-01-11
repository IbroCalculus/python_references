import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = tk.Label(root, text='Enter Password:')
label.pack(side=tk.LEFT)

entry = ttk.Entry(root, show='*')
entry.pack(side=tk.LEFT)


root.mainloop()
