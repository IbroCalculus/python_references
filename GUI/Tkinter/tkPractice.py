import tkinter as tk

root = tk.Tk()
root.title("tkPractice Home Management System")
root.config(width=800, height=400, bg="#7AD2B1")
root.resizable(width=True, height=True)

photo = tk.PhotoImage(file='images/lock.png')
root.iconphoto(True, photo)

screenWidth = root.winfo_screenwidth()
screenHeigth = root.winfo_screenheight()

userNameLabel = tk.Label(root, text="Username: ", fg="black", font="Cherryla 12", relief="sunken")
# userNameLabel.pack()
userNameLabel.grid(row=0, column=0)

userNameEntry = tk.Entry(root, width=50)
userNameEntry.grid(row=0, column=1)

passwordLabel = tk.Label(root, text="Password: ", fg="black", font="Cherryla 12", relief="ridge")
# passwordLabel.pack()
passwordLabel.grid(row=1, column=0)

pswdEntry = tk.Entry(root, width=50, show='#')
pswdEntry.grid(row=1, column=1)

def loginUser():
    print("User Logged in successfully!!!")

btnLogin = tk.Button(root, text="LOGIN", bg="#3934C4", fg="#FFFFFF", font="Cherryla", command=loginUser)
btnLogin.grid(row=2, column=0)


print(btnLogin.keys())

print(f'The width and height respectively are: {screenWidth}, {screenHeigth}')


tk.mainloop()