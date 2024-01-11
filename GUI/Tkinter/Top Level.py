import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser as CCh


root = tk.Tk()

def openTopLevel():
    topLevel = tk.Toplevel()
    topLevel.title("Top Level window")
    topLevel.iconbitmap("Images/index.ico")

    def choose():
        result = CCh.askcolor(color='red', title='Pick your color', parent=topLevel)
        topLevel['bg'] = result[1]
    
    btn = tk.Button(topLevel, text='Choose background color', command=choose)
    btn.pack()

btn = tk.Button(root, text="OPEN TOP LEVEL WINDOW", command=openTopLevel)
btn.pack()


root.mainloop()
