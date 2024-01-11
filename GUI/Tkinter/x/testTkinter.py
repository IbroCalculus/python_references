import tkinter as tk

root1 = tk.Tk()
canvas = tk.Canvas(root1)
scroll_y = tk.Scrollbar(root1, orient="vertical", command=canvas.yview)

root = tk.Frame(canvas)

# group of widgets
for i in range(100):
    tk.Label(root, text='label %i' % i).pack()

for i in range(100):
    tk.Button(root, text='Button'+str(i)).pack()

    

# put the frame in the canvas
canvas.create_window(0, 0, anchor='nw', window=root)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'), 
                 yscrollcommand=scroll_y.set)
                 
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')

root1.mainloop()
