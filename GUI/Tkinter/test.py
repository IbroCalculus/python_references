import tkinter as tk
from tkinter import ttk


root = tk.Tk()

root.config(bg='#00A2FF')
root.geometry("800x400")
root.wm_attributes("-alpha", 0.5)

selection1 = tk.StringVar()
radio1 = tk.Radiobutton(root, text="First", variable=selection1, value=1)
radio1.select()
radio1.pack()

radio2 = tk.Radiobutton(root, text="Second", variable=selection1, value=2)
# radio2.deselect()
radio2.pack()

radio3 = tk.Radiobutton(root, text="Third", variable=selection1, value=3)
# radio3.deselect()
radio3.pack()

selection2 = tk.StringVar()
radio11 = tk.Radiobutton(root, text="First", variable=selection2, value=1)
# radio1.select()
radio11.pack()

radio21 = tk.Radiobutton(root, text="Second", variable=selection2, value=2)
radio21.select()
radio21.pack()

radio31 = tk.Radiobutton(root, text="Third", variable=selection2, value=3)
# radio3.deselect()
radio31.pack()



root.mainloop()
