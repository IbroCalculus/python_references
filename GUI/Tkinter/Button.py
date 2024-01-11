import tkinter as tk
from tkinter import ttk


root = tk.Tk()

def firstCommand():
    print("You clicked on button 1")

def secondCommand():
    print("You clicked on button 2")

button1 = tk.Button(root, text="FIRST BUTTON", bg="red", fg="white", font="Cherryla", command=firstCommand)
button1.pack()

button2 = ttk.Button(root, text="SECOND BUTTON", command=secondCommand)
button2.pack()

button2 = ttk.Button(root, text="DISABLED", state=tk.DISABLED)
button2.pack()

print(button1.keys())
print("\n")
print(button2.keys())


root.mainloop()
