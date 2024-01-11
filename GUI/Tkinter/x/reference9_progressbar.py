import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()


def progress(currentValue):
    progressbar["value"]=currentValue

maxValue = 100

progressbar=ttk.Progressbar(root,orient="horizontal",length=300,mode="determinate")
progressbar.pack(side=tk.TOP)

currentValue=0
progressbar["value"]=currentValue
progressbar["maximum"]=maxValue

divisions=10
for i in range(divisions):
    currentValue=currentValue+10
    progressbar.after(500, progress(currentValue))
    progressbar.update() # Force an update of the GUI

root.mainloop()
