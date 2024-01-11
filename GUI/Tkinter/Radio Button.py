import tkinter as tk
from tkinter import ttk


root = tk.Tk()

selection1 = tk.StringVar()
radio1 = tk.Radiobutton(root, text="First", variable=selection1, value=1)
radio1.select()
radio1.pack()

radio2 = tk.Radiobutton(root, text="Second", variable=selection1, value=2)
radio2.deselect()

radio3 = tk.Radiobutton(root, text="Third", variable=selection1, value=3)
radio3.deselect()
radio3.pack()



selection2 = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Next First", variable=selection2, value=1)
radio1.select()
radio1.pack()

radio2 = tk.Radiobutton(root, text="Next Second", variable=selection2, value=2)
radio2.deselect()
radio2.pack()

radio3 = tk.Radiobutton(root, text="Next Third", variable=selection2, value=3)
radio3.deselect()
radio3.pack()

root.mainloop()
