import tkinter as tk
from tkinter import ttk


root = tk.Tk()

chk = tk.Checkbutton(root, text='Click to check')
chk.pack()

chk1 = ttk.Checkbutton(root, text='Click to check')
chk1.pack()

spacer = tk.Label(root, text='\n')
spacer.pack()

checkDis = tk.Checkbutton(root, text='DISABLED', state=tk.DISABLED)
checkDis.pack()

checkEn = tk.Checkbutton(root, text='ENABLED but deselected')
checkEn.deselect()
checkEn.pack()

def display():
    if stateVar.get() =='yes':
        print("Checked")
        label['text'] = "Checked"
    elif stateVar.get() == 'no':
        print("UNCHCECKED")
        label['text'] = "UNCHECKED"

stateVar = tk.StringVar()
checkEn2 = tk.Checkbutton(root, text='ENABLED and selected', variable=stateVar,
                          onvalue='yes', offvalue='no',
                          command=display)
checkEn2.select()
checkEn2.pack()

label = tk.Label(root, text="Awaiting Checkbutton")
label.pack()

print(chk.keys())

root.mainloop()
