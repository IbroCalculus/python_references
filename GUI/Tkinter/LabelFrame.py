import tkinter as tk

root = tk.Tk()

labelFrame = tk.LabelFrame(root, text='This is a label frame')
labelFrame.pack()

tk.Label(labelFrame, text="Label1", width=30).grid(column=0, row=0, sticky=tk.W)
tk.Label(labelFrame, text="Label2", width=30).grid(column=1, row=0)
tk.Label(labelFrame, text="Label3", width=30).grid(column=2, row=0)
tk.Entry(labelFrame, width=30).grid(column=0,row=2, pady=10)

btn = tk.Button(labelFrame, text="CLICK")
btn.grid(row=2, column=1)

root.mainloop()