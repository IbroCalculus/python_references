import tkinter as tk
from tkinter import filedialog as fd

#METHODS
#    fd.askopenfile()
#    fd.askdirectory()
#    fd.askopenfiles()
#    fd.askopenfilename()
#    fd.asksaveasfile()
#    fd.askopenfilenames()
#    fd.asksaveasfilename()

root = tk.Tk()

def openFile():
    filename = fd.askopenfilename()
    print(filename)
    lbl['text'] = filename

btn = tk.Button(root, text='Choose file', command=openFile)
btn.pack()

lbl = tk.Label(root, text='Awaiting text')
lbl.pack()


root.mainloop()