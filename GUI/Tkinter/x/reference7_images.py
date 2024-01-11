import tkinter as tk

root = tk.Tk()

pic1 = 'icons8_note_64.png'
Image = tk.PhotoImage(file = pic1)

label1 = tk.Label(width=100, image=Image)
label1.pack()


pic2 = 'giphy.gif'
frame2 = tk.PhotoImage(file = pic2, format='gif -index 1')
label2 = tk.Label(width=100, image=frame2)
label2.pack()

root.mainloop()
