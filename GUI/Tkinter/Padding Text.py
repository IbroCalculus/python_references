import tkinter as tk

root = tk.Tk()

label_1 = tk.Label(root, text="This is the first text", bg="red")
label_1.pack()


label_2 = tk.Label(root, text="This is the second text", bg="green",
                   fg="white", font="Bloodlust 20", padx=50, pady=50)
label_2.pack()

label_3 = tk.Label(root, text="This is the third text", bg="blue", bd=5, relief="groove", width=100, height=4,
                   fg="white", font="Bloodlust 20", pady=50, padx=100, anchor=tk.N)
label_3.pack()

root.mainloop()
