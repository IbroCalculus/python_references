from tkinter import filedialog, messagebox
import tkinter as tk
import tkinter.scrolledtext as ScrolledText
import os


# root window
root = tk.Tk()
root.title("Ibrahim's Personal Text Editor")
root.iconbitmap('images/icons8_note_64.ico')
textArea = ScrolledText.ScrolledText(root, width=100, height=100)
textArea.pack()

#---------------FUNCTIONS---------------------

#NewFile():
def newFile():
    if len(textArea.get('1.0', END+'-1c')) > 0:
        result = messagebox.askyesno('Save?', "Do you wish to save?")
        if result:
            saveFile()
            

#openFile
def openFile():
    file = filedialog.askopenfile(parent=root, title='Select a text file', filetypes=(("Text files", "*.txt"),("All files",'*.*')))

    root.title(os.path.basename(file.name) + " - TEXT EDITOR")
    if file !=None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()

def quitMain():
    result = messagebox.askyesno('QUIT', 'Sure to quit?')
    if result:
        root.destroy()

def about():
    messagebox.showinfo('About', 'Designed and Developed by:\nTheEngineeringScientist\n             CONTACT   \nEmail: thebizzzbuzzz@gmail.com\nMobile: +234-816-819-4237')

#menu bar
menu = tk.Menu(root)
root.config(menu=menu)

#filemenu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save')
filemenu.add_command(label='Print')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=quitMain)

#helpmenu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Help')
helpmenu.add_command(label='About',command=about)



# looping through the codes starting from root
root.mainloop()
