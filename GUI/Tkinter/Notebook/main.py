import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("MAIN FILE")
root.geometry('600x600')

img1 = tk.PhotoImage(file='imagefiles/icons8_note_64.png')
img2 = tk.PhotoImage(file='imagefiles/icons8_ball_point_pen_filled_64.png')

s = ttk.Style()
s.configure("TNotebook", background='green', borderwidth=3)
s.configure("TNotebook.Tab", background='red', foreground='orange', borderwidth=4)
s.configure("TFrame", background='yellow', foreground='brown', borderwidth=0)


tabControl = ttk.Notebook(root, style='TNotebook')

tab1 = ttk.Frame(tabControl, style='TFrame')
tabControl.add(tab1, text="TAB 1", image=img1, compound=tk.TOP)

tab2 = ttk.Frame(tabControl, style='TFrame')
tabControl.add(tab2, text="TAB 2", image=img2, compound=tk.BOTTOM)

tab3 = ttk.Frame(tabControl, style='TFrame')
tabControl.add(tab3, text="TAB 3", image=img2, compound=tk.RIGHT)

tab4 = ttk.Frame(tabControl, style='TFrame')
tabControl.add(tab4, text="TAB 4", image=img2, compound=tk.LEFT)

tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text="TAB 5")


btn1 = tk.Button(tab1, text='This is a button FOR TAB 1')
btn1.pack()


btn2 = tk.Button(tab2, text='FOR TAB 2')
btn2.pack()

btn3 = tk.Button(tab3, text='TAB 3 BUTTON')
btn3.pack()



tabControl.pack(expand=1, fill='both')

root.mainloop()
