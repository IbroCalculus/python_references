import tkinter as tk
from tkinter import messagebox as mbox


root = tk.Tk()

def right_mouse(event):
    label['text'] = "You RIGHT-clicked the mouse"
    label['bg']='red'
    
def left_mouse(event):
    label['text'] = "You LEFT-clicked the mouse"
    label['bg']='green'
    
def center_mouse(event):
    label['text'] = "You CENTER-clicked the mouse"
    label['bg']='blue'


button = tk.Button(text='CLICK WITH MOUSE')
button.bind('<Button-1>', left_mouse)
button.bind('<Button-2>', center_mouse)
button.bind('<Button-3>', right_mouse)
button.pack()

label = tk.Label(root, text='Awaiting click')
label.pack()



root.mainloop()
