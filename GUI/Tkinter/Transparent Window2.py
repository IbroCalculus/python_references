import tkinter as tk

root = tk.Tk()
root.state('zoomed')
root.geometry('400x300')
root.config(bg='#00A2FF')
root.attributes("-transparentcolor", "red")

root.mainloop()