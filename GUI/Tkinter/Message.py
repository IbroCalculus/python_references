import tkinter as tk

root = tk.Tk()

msg = tk.Message(root,
                 text="This is a Message widget, It is similar to a label, rather, it displays multiline texts",
                 width=50, bg='red')
msg.pack(anchor=tk.W)


msg1 = tk.Message(root,
                 text="This is another Message widget, It is similar to a label, rather, it displays multiline texts",
                 width=50)
msg1.pack(anchor=tk.NE)

root.mainloop()