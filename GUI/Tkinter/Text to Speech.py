import tkinter as tk
import pyttsx3

root = tk.Tk()

engine = pyttsx3.init()
engine.say("Hello, I am Ibrahim")
engine.runAndWait()

root.mainloop()
