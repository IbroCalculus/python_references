import tkinter as tk

root = tk.Tk()

label_1 = tk.Label(root, text="This is the first line\nSecond\nAnd this is the longest of all, the third", font="Bloodlust 30", bg="red", fg='white', justify=tk.RIGHT)
label_1.pack()

#Justify values are: RIGHT, LEFT and CENTER


root.mainloop()
