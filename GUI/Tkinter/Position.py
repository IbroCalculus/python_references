import tkinter as tk

root = tk.Tk()

#Check also, Anchor

#root.geometry("200x400+100+200")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_pos = screen_width/4
y_pos = screen_height/4

root.geometry("%dx%d+%d+%d" % ((screen_width/2), (screen_height/2), x_pos, y_pos))

root.mainloop()
