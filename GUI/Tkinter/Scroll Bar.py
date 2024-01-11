import tkinter as tk

root = tk.Tk()


frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fil=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set,
                     activestyle='dotbox', bg='red', bd=4, fg='#fff', relief=tk.RAISED,
                     selectmode=tk.EXTENDED)
listbox.insert(tk.END, "First List")
listbox.insert(tk.END, "Second List")
names = ["Ibrahim", "Musa", "Suleiman", "Ibrahim", "Musa", "Suleiman", "Ibrahim", "Musa", "Suleiman",
         "Ibrahim", "Musa", "Suleiman", "Ibrahim", "Musa", "Suleiman", "Ibrahim", "Musa", "Suleiman"]
for i in names:
    listbox.insert(tk.END, i)
listbox.pack()

scrollbar.config(command=listbox.yview)


root.mainloop()