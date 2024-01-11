import tkinter as tk

root = tk.Tk()

def getMousePosition(event):
    x_pos = str(event.x)
    y_pos = str(event.y)
    
    label['text'] = "You clicked @: {}, {}".format(x_pos, y_pos)

root.bind('<Button-1>', getMousePosition)

button = tk.Button(root, text='CLICK TO GET THE POSITION  OF THE MOUSE')
button.bind('<Button-1>', getMousePosition)
button.pack()


label = tk.Label(root, text='Awaiting Mouse Click')
label.pack()


root.mainloop()
