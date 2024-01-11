import tkinter as tk

root = tk.Tk()

listbox = tk.Listbox(root, activestyle='dotbox', bg='red', bd=4, fg='#fff', relief=tk.RAISED,
                     selectmode=tk.EXTENDED)
listbox.insert(tk.END, "First List")
listbox.insert(tk.END, "Second List")
names = ["Ibrahim", "Musa", "Suleiman", "Ibrahim", "Musa", "Suleiman", "Ibrahim", "Musa", "Suleiman",
         "Ibrahim", "Musa", "Suleiman", "Ibrahim", "Musa", "Suleiman", "Ibrahim", "Musa", "Suleiman"]
for i in names:
    listbox.insert(tk.END, i)
listbox.pack()

#For scrollview ability, check Scroll Bars

root.mainloop()