import tkinter as tk
from tkinter import ttk

#No tk.Combobox, only ttk.Combobox

root = tk.Tk()

selection = tk.StringVar()
combo = ttk.Combobox(root, textvariable=selection,
                     width=20, values=(1,2,3))


options = ('Monday', "Tuesday", 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
combo = ttk.Combobox(root, textvariable=selection, state='readonly',
                     width=20, values=options, foreground='red',
                     background='green')
combo.current(0)
combo.pack()
print(combo.keys())

def display():
    label['text'] = selection.get()

btn = tk.Button(root, text='CLICK HERE', command=display)
btn.pack()

label = tk.Label(root, text='Awaiting display')
label.pack()



root.mainloop()
