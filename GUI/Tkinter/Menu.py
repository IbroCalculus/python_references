import  tkinter as tk
from tkinter import messagebox as mbox


root = tk.Tk()

icon_new = tk.PhotoImage(file='Images/new_file.gif')
icon_redo = tk.PhotoImage(file="Images/redo.gif")

def msg():
    mbox.showinfo("INFO", "Message lies here")


menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='New Project', compound='right', image=icon_new)
filemenu.add_command(label='New', accelerator='Ctrl + N', image=icon_redo, compound='left', command=msg) #size 16 x 16
filemenu.add_separator()
filemenu.add_command(label='Exit', underline=1, command=quit)
menubar.add_cascade(label="File", menu=filemenu)


editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label='Undo')
editmenu.add_command(label='Copy', accelerator='Ctrl + C')
editmenu.add_command(label='Cut')
menubar.add_cascade(label='Edit', menu=editmenu)


othermenu = tk.Menu(menubar, tearoff=0)
othermenu.add_checkbutton(label='Check here', accelerator='Check + C')
othermenu.add_radiobutton(label='Radio here', accelerator='Radio + R')
menubar.add_cascade(label='Others', menu=othermenu)

#To add submenus, check reference


root.mainloop()