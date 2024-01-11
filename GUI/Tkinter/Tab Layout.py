import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox as mbox

root = tk.Tk()

lockPhoto = tk.PhotoImage(file='Images\lock.png')
facebookPhoto = tk.PhotoImage(file=r'Images\facebook.png')
searchPhoto = tk.PhotoImage(file=r'Images\search.png')


s = ttk.Style()
s.configure("TNotebook", background='green', borderwidth=3)
s.configure("TNotebook.Tab", background='red', foreground='orange', borderwidth=4)
s.configure("TFrame", background='#00A2FF', foreground='brown', borderwidth=0)

tabControl = ttk.Notebook(root, style="TNotebook")

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1', image=lockPhoto)
tabControl.add(tab2, text='Tab 2', image=facebookPhoto, compound=tk.TOP)
tabControl.add(tab3, text='Tab 3', image=searchPhoto, compound=tk.RIGHT)
tabControl.add(tab4, text='Tab 4')
tabControl.pack(expand=1, fill=tk.BOTH)

tk.Label(tab1, text='This is tab One', font='Cherryla 20').pack()
tk.Label(tab2, text="This is tab Two", font='Cherryla 30', fg='red').pack()
tk.Label(tab3, text='This is tab THREE', font='Cherryla 40', fg='green').pack()
tk.Label(tab4, text="This is tab Four", font='Cherryla 50', fg='blue').pack()



icon_new = tk.PhotoImage(file='Images/new_file.gif')
icon_redo = tk.PhotoImage(file="Images/redo.gif")

def msg():
    mbox.showinfo("INFO", "Message lies here")


menubar = tk.Menu(tab1)
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


root.mainloop()