import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text='\n').pack()
progressbar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=600, value=40, mode='indeterminate',
                              maximum=30)
progressbar.pack()
progressbar.start()
print(progressbar.keys())

progressbar1 = ttk.Progressbar(root, orient=tk.VERTICAL, length=300, mode='determinate')
progressbar1.pack()
progressbar1.start()
progressbar.step(4)
progressbar['value'] = 0
progressbar['maximum'] = 100
print(progressbar.keys())


root.mainloop()