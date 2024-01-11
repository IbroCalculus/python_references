import tkinter as tk
from tkinter import ttk


root = tk.Tk()

photo = tk.PhotoImage(file='images/picture.png')

label = tk.Label(root, image=photo)
label.pack()

button = tk.Button(root, image=photo, bd=3, relief=tk.GROOVE)
button.pack()


root.mainloop()
