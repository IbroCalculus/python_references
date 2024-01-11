import tkinter as tk



root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=200, bg='red')

canvas1.create_line(0,0,400,200,fill='blue', width=6)
canvas1.create_line(20,60,300,180,fill='green', width=6,dash=(10,1,2,1))

canvas1.pack()

def delete_canvas():
    canvas1.delete("all")

button = tk.Button(root, text="DELETE", command=delete_canvas)
button.pack()


canvas2 = tk.Canvas(root, width=400, height=200, bg='blue')
canvas2.pack()
root.mainloop()
