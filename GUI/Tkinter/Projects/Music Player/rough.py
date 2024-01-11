import tkinter as tk
import pygame as p
from tkinter import messagebox as mbox

root = tk.Tk()
root.iconbitmap("Images/music.ico")

root.title("CUSTOMIZED MUSIC PLAYER")
root.resizable(False, False)
root.wm_attributes("-alpha", 1)

screen_width = 1366
screen_height = 768
x_pos = screen_width / 4
y_pos = screen_height / 4
root.geometry("%dx%d+%d+%d" % ((screen_width / 2), (screen_height / 2), x_pos, y_pos))
root.config(bg='#00A2FF')


menubar = tk.Menu(root)
root.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='New Project', compound='right')
filemenu.add_command(label='New', accelerator='Ctrl + N', compound='left') #size 16 x 16
filemenu.add_separator()
filemenu.add_command(label='Exit', underline=1, command=quit)
menubar.add_cascade(label="File", menu=filemenu)

def showDev():
    mbox.showinfo("Developer Info", "Designed and developed by:\nIbrahim Suleiman\nContact: ibsuleiman9@gmail.com")

aboutmenu = tk.Menu(menubar, tearoff=0)
aboutmenu.add_command(label='About Software', command=showDev)
menubar.add_cascade(label="About", menu=aboutmenu)


PhotoPlay = tk.PhotoImage(file='Images/play.png')
PhotoPause = tk.PhotoImage(file="Images/pause.png")
PhotoStop = tk.PhotoImage(file='Images/stop.png')

p.mixer.init()          #Initialize Pygame mixer

def playMusic():
    try:
        paused
    except NameError:
        p.mixer.music.load("Sounds/sound1.mp3")
        p.mixer.music.play()
        p.mixer.music.set_volume(0.5)
    else:
        p.mixer.music.unpause()
        p.mixer.music.set_volume(0.5)

def stopMusic():
    p.mixer.music.stop()

def pauseMusic():
    global paused
    paused = True
    p.mixer.music.pause()

btnPlay = tk.Button(root, image=PhotoPlay, command=playMusic)
btnPlay.pack()

btnStop = tk.Button(root, image=PhotoStop, command=stopMusic)
btnStop.pack()

btnStop = tk.Button(root, image=PhotoPause, command=pauseMusic)
btnStop.pack()


def vol(ev=None):
    x = volume.get()
    val = x*0.1
    print(val)
    p.mixer.music.set_volume(int(val))

volume = tk.Scale(root, orient=tk.HORIZONTAL, from_=0, to=100, command=vol)
volume.set(50)
volume.pack()

root.mainloop()