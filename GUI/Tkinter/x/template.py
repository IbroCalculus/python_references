import tkinter as tk

root = tk.Tk()
root.title("This is my template")
root.config(bg='red')
print(id(root), type(root))

root.mainloop()
