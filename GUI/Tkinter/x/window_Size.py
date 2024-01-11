import tkinter as tk

root = tk.Tk()
root.title("This is my template")
root.config(bg='#123456')
root.resizable(width=True, height=True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#x+y offset
#root.geometry("400x200+800+200")

root.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 200, 300))

label = tk.Label(root, text='This is a text', bg='red',
                 activebackground='blue', bd=10)
label.pack()

label2 = tk.Label(root, text="This is another text", activeforeground='yellow', relief='solid', bd=10)
label2.pack()

root.mainloop()
