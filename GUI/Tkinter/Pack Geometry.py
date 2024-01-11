import tkinter as tk
from tkinter import ttk

#Some pack properties: side, fill, anchor, expand

root = tk.Tk()
root.title("Playing with Frames and Pack geometry manager")
topFrame = tk.Frame(root, bg='red', width=800, height=10, bd=2, relief=tk.GROOVE)
bottomFrame = tk.Frame(root)
topFrame.pack()

spacer0 = tk.Label(root, text="\n")
spacer0.pack()

bottomFrame.pack()

label1 = tk.Label(topFrame, text="First Label in first Frame", height=10, width=10, bg='green')
label1.pack()


label2 = tk.Label(topFrame, text="Second Label in first Frame")
label2.pack()

label1 = tk.Label(bottomFrame, text="First Label in first Frame", bg='lightblue')
label1.pack(side=tk.LEFT)

label2 = tk.Label(bottomFrame, text="Second Label in first Frame", bg='darkblue')
label2.pack()

spacer = tk.Label(root, text="\n")
spacer.pack()

label3 = tk.Label(root, text="Check this out", pady=20, bg='purple', underline=0)
label3.pack(fill=tk.X)

label4 = tk.Label(root, text="and this out", pady=20, bg='indigo', underline=1)
label4.pack(side = tk.RIGHT, fill=tk.BOTH)


root.mainloop()
