from tkinter import *

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry(str(width) + "x" + str(height+500))
w=Canvas(root, bg='purple', width=width-22, height=height, scrollregion=(0,0,400,18500))# XXX----
hbar=Scrollbar(root,width=20,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=w.xview)
vbar=Scrollbar(root, width=20, orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=w.yview)
w.config(width=width-22,height=height-25)
w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
w.pack(side=LEFT,expand=True,fill=BOTH)
# YOUR APP FRAME HERE
top=Frame(w, width=str(width-22), height=str(height),
background='#cecece', relief=FLAT)
w.create_window(0, 0, window=top, anchor="nw")
