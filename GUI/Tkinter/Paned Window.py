import tkinter as tk

root = tk.Tk()

paned = tk.PanedWindow(root, bd=4, relief=tk.GROOVE, bg='red')
paned.pack(fill=tk.BOTH, expand=1)

root.mainloop()
