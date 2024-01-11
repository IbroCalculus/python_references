import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

root = tk.Tk()
root.geometry('400x400')
tabFrame = tk.Frame(root)
tabFrame.pack()
otherFrame = tk.Frame(root)
otherFrame.pack()

#toolpit class
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        
    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
        background="#ffffe0", relief=tk.SOLID, borderwidth=1,
        font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
        
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
#===========================================================
def createToolTip( widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

#tab and Notebook
tabControl = ttk.Notebook(tabFrame)
tab1 = tk.Frame(tabControl)
tab2 = tk.Frame(tabControl)
tab3 = tk.Frame(tabControl, bg='blue')

tabControl.add(tab1, text='TAB1')
tabControl.add(tab2, text='TAB2')
tabControl.add(tab3, text='TAB3')

tabControl.pack(expand='yes', fill='both')


# Using a scrolled Text control
scrolW = 30; scrolH = 3
scr = scrolledtext.ScrolledText(tab1, width=scrolW, height=scrolH,
wrap=tk.WORD)
scr.grid(column=0, row=1, sticky='WE', columnspan=3)
# Add a Tooltip to the ScrolledText widget
createToolTip(scr, 'This is a ScrolledText widget.')

btn1 = tk.Button(tab1, text='This is a button')
btn1.grid(row=2, column=0)
# Add a Tooltip to the btn1 widget
createToolTip(btn1, 'This is a button widget.')

#Canvass in tab3

for orangeColor in range(2):
    canvas = tk.Canvas(tab3, width=150, height=80,
                       highlightthickness=0, bg='orange')
    canvas.grid(row=orangeColor, column=orangeColor)

#variables
strVar = tk.StringVar()
intVar = tk.IntVar()
doubleVar = tk.DoubleVar()
boolVar = tk.BooleanVar()

nameEntry = tk.Entry(otherFrame, textvariable=strVar)
strVar.set('Ibrahim')
nameEntry.grid(row=0, column=0)
nameEntry.focus()

dispLabel = tk.Label(otherFrame, text='')
dispLabel.grid(row=0, column=2)

def f():
    data = strVar.get()
    msg = 'You are welcome Mr '+data
    dispLabel['text'] = msg

btn = tk.Button(otherFrame, text='Click', command=f)
btn.grid(row=0, column=1)

root.mainloop()
