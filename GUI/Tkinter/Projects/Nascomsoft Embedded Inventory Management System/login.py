import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
import os

root = tk.Tk()
root.iconbitmap(r'Images/nascomsoft2.ico')
root.title("NASCOMSOFT EMBEDDED INVENTORY MANAGEMENT SYSTEM")
root.resizable(False, False)
root.wm_attributes("-alpha", 0.9)

screen_width = 1366
screen_height = 768
x_pos = screen_width / 4
y_pos = screen_height / 4
root.geometry("%dx%d+%d+%d" % ((screen_width / 2), (screen_height / 2), x_pos, y_pos))
root.config(bg='#00A2FF')

frame1 = tk.Frame(root, bg='#00A2FF')
tk.Label(frame1, text='NASCOMSOFT EMBEDDED', fg="#fff", bg='#00A2FF', font="EthnocentricRg-regular 18").pack()

photo = tk.PhotoImage(file='Images/lock.png')
label = tk.Label(frame1, image=photo)
label.pack()
frame1.pack()

spacer = tk.Label(root, text='', bg='#00A2FF')
spacer.pack()

frame2 = tk.Frame(root, bg='#00A2FF', width=(screen_width / 2))
label_username = tk.Label(frame2, text="Enter Username: ", bg='#00A2FF', fg='#fff', justify=tk.LEFT, font='Times 14',
                          anchor=tk.W)
label_username.grid(row=0, column=0, sticky=tk.W)
entry_username = tk.Entry(frame2, font='Times 14')
entry_username.grid(row=0, column=1)
entry_username.focus()

tk.Label(frame2, text="\n", bg='#00A2FF', fg='#00A2FF').grid(row=1)

label_password = tk.Label(frame2, text="Enter Password: ", bg='#00A2FF', fg='#fff', justify=tk.LEFT, font='Times 14',
                          anchor=tk.W)
label_password.grid(row=2, column=0)
entry_password = tk.Entry(frame2, show='*', font='Times 14')
entry_password.grid(row=2, column=1)

tk.Label(frame2, text='', bg='#00A2FF').grid(row=3)


def openMain():
    '''
    root1 = tk.Toplevel()
    root1.iconbitmap(r'Images/nascomsoft2.ico')
    root1.title("NASCOMSOFT EMBEDDED INVENTORY MANAGEMENT SYSTEM")

    screen_width = 1366
    screen_height = 768
    root1.geometry("%dx%d+%d+%d" % ((screen_width), (screen_height), 0, 0))
    root1.config(bg='#00A2FF')
'''


def loginCommand():
    x = entry_username.get()
    y = entry_password.get()
    print(x)
    if x == 'nascomsoft' and y == '1234':
        print('Login Successful')
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        # openMain()

    else:
        print('Wrong login details')
        mbox.showerror("LOGIN CREDENETIALS ERROR", "Wrong user name or password")


btn_Login = tk.Button(frame2, text='Login', bg='#fff', bd=2, relief=tk.GROOVE, width=10, command=loginCommand)
btn_Login.grid(row=4, column=1, sticky=tk.E)

frame2.pack()

'''
label_username = tk.Label(frame2, text="Enter Username: ")
label_username.grid(row=0, column=0)

entry_username = tk.Entry(frame2)
entry_username.grid(row=0, column=1)

label_password = tk.Label(frame2, text="Enter Password: ")
label_password.grid(row=1, column=0)

entry_password = tk.Entry(frame2)
entry_password.grid(row=1, column=1)
btn_Login = tk.Button(root, text='Login')
btn_Login.grid(row=2, column=1)

frame2.pack()
'''

root.mainloop()
