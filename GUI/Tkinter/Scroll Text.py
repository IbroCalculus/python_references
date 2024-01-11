import tkinter as tk
from tkinter import scrolledtext


root = tk.Tk()

scroll = scrolledtext.ScrolledText(root, width=30, height=4, wrap=tk.WORD)
scroll.pack()


root.mainloop()