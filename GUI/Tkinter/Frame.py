import tkinter as tk
import tkinter as ttk


root = tk.Tk()
root.config(bg='#981234')

#Frame is similar to Div in HTML

topFrame = tk.Frame(root, bg="green",width=150, height=150, relief=tk.RAISED)
topFrame.config(bg='#00ff00')


label_1 = tk.Label(topFrame, text="Enter Firstname", font="Times 20")
label_1.pack()

label_2 = tk.Label(topFrame, text="Enter Middlename", font="Times 20")
label_2.pack()

label_3 = tk.Label(topFrame, text="Enter Surname", font="Times 20")
label_3.pack()

topFrame.grid(row=0, column=0)


bottomFrame = tk.Frame(root, bg="blue", width=150, height=250, bd=8, relief=tk.GROOVE)


label_11 = tk.Label(bottomFrame, text="Enter Firstname", font="Times 20", bg='blue', fg='white')
label_11.pack()

label_22 = tk.Label(bottomFrame, text="Enter Middlename", font="Times 20", bg='blue', fg='white')
label_22.pack()

label_33 = tk.Label(bottomFrame, text="Enter Surname", font="Times 20", bg='blue', fg='white')
label_33.pack()

bottomFrame.grid(row=1, column=1)

root.mainloop()
