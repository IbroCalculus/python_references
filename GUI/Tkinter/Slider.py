import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def disp(ev=None):
    label['text'] = slider.get()


def disp2(ev=None):
    label['text'] = slider1.get()
    slider['sliderlength'] = slider1.get()*10


slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=0, to=10, sliderlength=20,
                  bg='red', fg='red', tickinterval=2, troughcolor='yellow', relief=tk.FLAT,
                  showvalue=0, sliderrelief=tk.FLAT, width=5, font='Cherryla 1',
                  highlightthickness=5, command=disp)
slider.pack(anchor=tk.W)
print(slider.keys())

slider1 = ttk.Scale(root, orient=tk.HORIZONTAL, from_=0, to=10, command=disp2)
slider1.pack()
print(slider1.keys())

label = tk.Label(root, text='Awaiting slider change')
label.pack()

root.mainloop()
