import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
import os

root1 = tk.Tk()
root1.iconbitmap(r'Images/nascomsoft2.ico')
root1.title("NASCOMSOFT EMBEDDED INVENTORY MANAGEMENT SYSTEM")

screen_width = 1366
screen_height = 768
x_pos = screen_width / 4
y_pos = screen_height / 4
root1.geometry("%dx%d+%d+%d" % ((screen_width), (screen_height), 0, 0))
root1.config(bg='#00A2FF')

frame1 = tk.Frame(root1, width=1366)
tk.Label(frame1, text='NASCOMSOFT EMBEDDED INVENTORY', width=1366, height=1, fg='#fff', bg='#00A2FF',
         font="Ethnocentric 24").pack()
frame1.pack()

frame2 = tk.Frame(root1, width=1355)
lbl_component = tk.Label(frame2, text='COMPONENT')
lbl_component.pack(side=tk.LEFT)
frame2.pack()

root1.mainloop()
