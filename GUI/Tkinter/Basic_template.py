import tkinter as tk

root = tk.Tk()

radio1 = tk.Radiobutton(root, text="First", variable=selection1, value=1)
radio1.select()
radio1.pack()




root.mainloop()
