import tkinter as tk


root = tk.Tk()

label_1 = tk.Label(root, text="This is Label 1", font="Times 24", bg="red", bd=5)
label_1.grid(row=0, column=0)

label_2 = tk.Label(root, text="This is Label 2", font="Times 24", bg="blue")
label_2.grid(row=1, column=0)


label_1 = tk.Label(root, text="This is Label 1", font="Times 24", bg="red")
label_1.grid(row=2, column=0)

label_2 = tk.Label(root, text="This is Label 2", font="Times 24", bg="blue")
label_2.grid(row=2, column=1)

labelUser = tk.Label(root, text='Username')
labelUser.grid(row=3, column=0, sticky=tk.E)

labelPass = tk.Label(root, text='Password')
labelPass.grid(row=4, column=0, sticky=tk.W)

entryUser = tk.Entry(root, text='Username')
entryUser.grid(row=3, column=1, sticky=tk.E)

entryPass = tk.Entry(root, text='Password', justify=tk.RIGHT)
entryPass.grid(row=4, column=1, sticky=tk.W)







root.mainloop()
