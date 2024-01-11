import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox

#There are 7 common types of pop-ups

root = tk.Tk()
root.iconbitmap(r'Images/index3.ico')

def messagebox1():
    mbox.showinfo("INFO", "Message lies here")

def messagebox2():
    mbox.showwarning("WARNING", "Message lies here")

def messagebox3():
    mbox.showerror("ERROR", "Message lies here")

def messagebox4():
    reply = mbox.askokcancel("TITLE HERE", "Message lies here")
    if reply == True:
        print("You selected OK")
    elif reply == False:
        print("you selected CANCEL")

def messagebox5():
    reply = mbox.askquestion("TITLE HERE", "Message lies here")
    if reply == 'yes':
        print("You selected YES")
    elif reply =='no':
        print("you selected NO")

def messagebox6():
    reply = mbox.askyesno("TITLE HERE", "Message lies here")
    if reply == True:
        print("You selected YES")
    elif reply == False:
        print("you selected NO")

def messagebox7():
    reply = mbox.askretrycancel("TITLE HERE", "Message lies here")
    if reply == True:
        print("You selected RETRY")
    elif reply == False:
        print("you selected CANCEL")


btn1 = tk.Button(root, text="Show Info", command=messagebox1)
btn1.pack()

btn2 = tk.Button(root, text="show Warning", command=messagebox2)
btn2.pack()

btn3 = tk.Button(root, text="show Error", command=messagebox3)
btn3.pack()

btn4 = tk.Button(root, text="Ask Ok Cancel", command=messagebox4)
btn4.pack()

btn5 = tk.Button(root, text="Ask Question", command=messagebox5)
btn5.pack()

btn6 = tk.Button(root, text="Ask Yes No", command=messagebox6)
btn6.pack()

btn6 = tk.Button(root, text="Ask Retry", command=messagebox7)
btn6.pack()


root.mainloop()
