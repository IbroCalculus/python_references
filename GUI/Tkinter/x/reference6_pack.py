import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text='This is text 1')
label.pack()

labe2 = tk.Label(root, text='This is text 2')
labe2.pack(padx=20, pady=40)


root.mainloop()
