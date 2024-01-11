import pygame as p
import time

p.mixer.init()              #Initialize the mixer, FIRST THING TO DO

#Playing Music with Pygame

def playMusic():
    try:
        paused      #Checks if paused variable is initialized
    except NameError:
        p.mixer.music.load("Sounds/sound1.mp3")
        p.mixer.music.play()
    else:
        p.mixer.music.unpause()         #If paused is initialized, do the else statement

def pauseMusic():
    global paused
    paused = True
    p.mixer.music.pause()

def stopMusic():
    p.mixer.music.stop()

#Volume control

x = input('Enter command:')
if x == 'play':
    playMusic()
    time.sleep(5)
