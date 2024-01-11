import tkinter as tk

root = tk.Tk()

# Units in pixels
#root.config(width=400, height=200, bg="#123455")
#root.geometry("400x200")
#root.geometry("400x200+0+0")

#root.resizable(width=False, height=True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_pos = screen_width/4
y_pos = screen_height/4

root.geometry("%dx%d+%d+%d" % ((screen_width/2), (screen_height/2), x_pos, y_pos)) #Display in middle

root.mainloop()
