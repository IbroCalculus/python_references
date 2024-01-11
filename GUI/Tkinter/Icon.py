import tkinter as tk

root = tk.Tk()

# root.iconbitmap(r'images/index.ico')

#If image is not in .ico format, rather png etc
photo = tk.PhotoImage(file='images/lock.png')
root.iconphoto(True, photo)


root.mainloop()
