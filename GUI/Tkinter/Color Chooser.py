import tkinter as tk
from tkinter import colorchooser as CCh

root = tk.Tk()

def colorChosen():
    result = CCh.askcolor(color='red', title='Pick your color', parent=root)
    root['bg'] = result[1]
    root.config('bg')

    print(result[1])
    print(result[0][0])
    print(result[0][1])
    print(result[0][2])

btn = tk.Button(root, text='CLICK TO PICK COLOR', command=colorChosen)
btn.pack()


root.mainloop()
