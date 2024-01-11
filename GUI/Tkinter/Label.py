import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_pos = screen_width / 4
y_pos = screen_height / 4

root.geometry("%dx%d+%d+%d" % (screen_width, screen_height, 0, 0))

label_1 = tk.Label(root, text="This is label 1", bg="#123456", fg="white", font="Cherryla 18")
label_1.pack()

label_2 = tk.Label(root, text="This is label 2", font="bloodlust 18 italic", fg='red')
label_2.pack()

label_3 = tk.Label(root, text="This is label 3", font="Malika 18", bg='red', width=5)
label_3.pack()

label_4 = tk.Label(root, text="This is label 4 \nSecond Line\nThird Line", font="Malika 18", bg='green', width=10)
label_4.pack()

label_5 = tk.Label(root, text="This is label 5", font="Malika 18", bg='red', fg="white", bd=5, relief="groove")
label_5.pack()

# RELIEF VALUES: 'solid', 'raised', 'ridge', 'sunken', 'groove', 'flat' OR tk.SOLID, tk.RAISED ...
# NB: Use either bd or borderwidth


root.mainloop()
