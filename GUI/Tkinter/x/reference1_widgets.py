import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root = tk.Tk()
root.iconbitmap(r'icons8_note_64.ico')
#root.geometry("600x400")


tkFrame = tk.Frame(root)
tkFrame.config(width=200)
ttkFrame = tk.Frame(root)
ttkFrame.config(width=200)
tkFrame.grid(row=0, column=0)
ttkFrame.grid(row=0, column=1)

#Labels
aL = tk.Label(root, text='This is a tk Label')
aL.grid(row=0, column=0)
bL = ttk.Label(root, text='This is a ttk Label')
bL.grid(row=0, column=1)

#Buttons
aBtn = tk.Button(root, text='This is a tk Button')
aBtn.grid(row=1, column=0)
aBtn.configure(state='disabled')
bBtn = ttk.Button(root, text='This is a ttk Button')
bBtn.grid(row=1, column=1)

#entry

aEntry = tk.Entry(root, width=20)
aEntry.grid(row=2, column=0)
bEntry = ttk.Entry(root, width=20)
bEntry.grid(row=2, column=1)
bEntry.focus()

#optionMenu
clicked = tk.StringVar()
clicked.set('Monday')

aBrop = tk.OptionMenu(root, clicked, "Monday","Tuesday","Wednesday")
aBrop.grid(row=3, column=0)
bBrop = ttk.OptionMenu(root, clicked, "Thursday","Friday","Saturday")
bBrop.grid(row=3, column=1)

#combobox
'''combo = tk.Combobox(root, values=('One','Two','Three'))
combo.grid(row=4, column=0)'''#Invalid attribute for tk
combo = ttk.Combobox(root, values=('Four','Five','Six'), state='readonly')
combo.grid(row=4, column=1)
combo.current(2)

#spinbox
spin = tk.Spinbox(root, from_=1, to=10, increment=1, width=10, bd=15)
spin.grid(row=5, column=0)
spin = ttk.Spinbox(root, from_=10, to=100, increment=10)
spin.grid(row=5, column=1, pady=10)

#checkbutton
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(root, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(row=6, column=0)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(root, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(row=6, column=1)

#radiobuttons tk
radVar = tk.IntVar()
rad1 = tk.Radiobutton(root, text='tkOne', variable=radVar, value=1)
rad1.grid(row=7, column=0)

rad2 = tk.Radiobutton(root, text='tkTwo', variable=radVar, value=2)
rad2.grid(row=7, column=1)

#radiobuttons ttk
radVar1 = tk.IntVar()
rad1 = ttk.Radiobutton(root, text='ttkFirst', variable=radVar1, value=1)
rad1.grid(row=8, column=0, sticky=tk.W)

rad2 = ttk.Radiobutton(root, text='ttkSecond', variable=radVar1, value=2)
rad2.grid(row=8, column=1)

#scrolledText tk
Swidth = 30
Sheight = 3
SArea = scrolledtext.ScrolledText(root, width=Swidth, height=Sheight,
                                  wrap=tk.WORD) #i.e tk.CHAR
SArea.grid(row=9, column=0)

#labelFrame
LFrame = ttk.LabelFrame(root, text='This is a label Frame')
LFrame.grid(row=10, column=0, sticky=tk.EW)

L1 = ttk.Label(LFrame, text='Label One').grid(row=0,column=0)
L2 = ttk.Label(LFrame, text='Label Two').grid(row=1,column=0)
L3 = ttk.Label(LFrame, text='Label Three').grid(row=2,column=0)
E1 = ttk.Entry(LFrame, width=20).grid(row=3)

LFrame2 = ttk.LabelFrame(root)
LFrame2.grid(row=10, column=1, padx=20, pady=40)

L1 = ttk.Label(LFrame2, text='Label One').grid(row=0,column=0)
L2 = ttk.Label(LFrame2, text='Label Two').grid(row=1,column=0, pady=10, padx=80)
L3 = ttk.Label(LFrame2, text='Label Three').grid(row=2,column=0)
E1 = ttk.Entry(LFrame2, width=20).grid(row=3, pady=10)

#Menus and Menubars
menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
editmenu = tk.Menu(menubar)
helpmenu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)
menubar.add_cascade(label='Help', menu=helpmenu)

filemenu.add_command(label='New')
filemenu.add_separator()

#exit function
def _quit():
    root.quit() #close the entire program
    root.destroy() #close the present window
    exit() #closes the python shell

#tabbed widgets / Notebook
def _tabs():
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='TAB1')
    tabControl.add(tab2, text='TAB2')
    tabControl.add(tab3, text='TAB3')

    tabControl.grid(row=0, column=0, sticky=tk.EW)

#messagebox
from tkinter import messagebox as mBox
def _msgBox():
     mBox.showinfo('INFO:','Developed by\nIbrahim Musa Suleiman\ncopyright: 2019')
     mBox.showwarning('WARNING:', 'This is a warning message')
     mBox.showerror('ERROR:','This is an error message')
     

def _mmsgBox():
    root.withdraw()
    ans = mBox.askyesno('YES OR NO:','Sure you want to quit?')
    if ans==True:
         print('Yes was selected')
    else: print('No was clicked')


filemenu.add_command(label='Exit', command=_quit)
editmenu.add_command(label='Edit', command=_tabs)
helpmenu.add_command(label='About...', command=_msgBox)
helpmenu.add_command(label='Help...', command=_mmsgBox)

root.config(menu=menubar)

#scrollbar
'''frame3 = tk.Frame(root)
frame3.grid(row=11, column=0)
scroll_bar = tk.Scrollbar(frame3)
frame3.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=frame3.yview)
scroll_bar.pack()
'''

#appearance / relief
spin1 = tk.Spinbox(root, values=(10,20,30,40,50))
spin1.grid(row=12, column=0, sticky=tk.W) #default: SUNKEN

spin2 = tk.Spinbox(root, from_=60, to=100, increment=10, bd=10, relief=tk.RAISED)
spin2.grid(row=12, column=1, sticky=tk.W)

spin3 = tk.Spinbox(root, values = (120,130,140,150,160), bd=10, relief=tk.FLAT)
spin3.grid(row=12, column=2)

spin4 = tk.Spinbox(root, values = (120,130,140,150,160), bd=10, relief=tk.GROOVE)
spin4.grid(row=12, column=3, padx=60)

spin5 = tk.Spinbox(root, values = (120,130,140,150,160), bd=10, relief=tk.RIDGE)
spin5.grid(row=12, column=4)


root.mainloop()
