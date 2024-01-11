
#Anchor is used to position The text within a widget. tk.E implies the text clings to the eastern part of the widget
#Justify == text align

import tkinter as tk

root = tk.Tk()

label_1 = tk.Label(root, text="This is the first Line\nAnd second\nNow here comes the third line which is longest",
                   font="Times 14", height=3, width=50, bd=5, relief="groove", bg= "red", anchor=tk.N, justify=tk.LEFT)
label_1.pack()

spacer = tk.Label(root, text="", height=4)
spacer.pack()


label_2 = tk.Label(root, text="This is the first Line\nAnd second\nNow here comes the third line which is longest",
                   font="Times 14", height=6, width=60, bd=5, relief="groove", bg= "red", anchor=tk.W, justify=tk.LEFT)
label_2.pack()

#Anchor values are N,E,W,S, NE, NW, SE, SW, CENTER


root.mainloop()
