import tkinter as tk

root = tk.Tk()

btn = tk.Button(root, text='Exit', command=quit)
btn.pack()


def destroy():
    root.destroy()


btn2 = tk.Button(root, text='Destroy', command=destroy)
btn2.pack()


root.mainloop()
