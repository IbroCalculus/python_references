
import tkinter as tk

root = tk.Tk()
root.title("Basic Calculator")

def calcFunc():
    pass



label_result = tk.Label(root, text=0000, width=10, height=10, bg="yellow")
label_result.grid(row=0, column=0, columnspan=3)

btn1 = tk.Button(root, text=1, width=10)
btn1.grid(row=1, column=0)
btn1 = tk.Button(root, text=2, width=10)
btn1.grid(row=1, column=1)
btn1 = tk.Button(root, text=3, width=10)
btn1.grid(row=1, column=2)

btn1 = tk.Button(root, text=4, width=10)
btn1.grid(row=2, column=0)
btn1 = tk.Button(root, text=5, width=10)
btn1.grid(row=2, column=1)
btn1 = tk.Button(root, text=6, width=10)
btn1.grid(row=2, column=2)

btn1 = tk.Button(root, text=7, width=10)
btn1.grid(row=3, column=0)
btn1 = tk.Button(root, text=8, width=10)
btn1.grid(row=3, column=1)
btn1 = tk.Button(root, text=9, width=10)
btn1.grid(row=3, column=2)


btn1 = tk.Button(root, text=0, width=10)
btn1.grid(row=4, column=0)

root.mainloop()