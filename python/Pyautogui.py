#check pyautogui document @pyautogui.readthedocs.io

import  pyautogui as pya
import time

DOWN = pya.keyDown('ctrl')

pya.FAILSAFE = True      #Move mouse to left top corner of monitor, raise exception FaisSafeEsception

#pya.PAUSE = 2           #Pause every pya action for 2 seconds after every action, Another fail safe

print(pya.size())
print(f'width = {pya.size()[0]}px, height = {pya.size()[1]}px')


#Moving the mouse
#pay.moveTo        moves the mouse relative to the screen position (0,0)
for i in range(1):
    pya.moveTo(100, 100, duration=1, tween=pya.easeInBounce)            #tween is mouse transition animation
    pya.moveTo(200, 100, duration=0.75, tween=pya.easeInOutElastic)     #Check for other tween options
    pya.moveTo(200, 200, duration=.5, tween=pya.easeInExpo)
    pya.moveTo(100, 200, duration=2, tween=pya.easeOutBounce)
pya.PAUSE = 2

#pya.moveRel(100, 200)      Moves the mouse relative to its current position


#Getting the mouse position
print("\n",pya.position())
print(f'The mouse is positioned @ x= {pya.position()[0]}, y = {pya.position()[1]}')
time.sleep(2)

#Clicking the mouse
pya.click(600,100)
time.sleep(2)
pya.click(button='right')
#pya.click(button='right', clicks=2, interval=0.25) will double click @ 0.25s interval
#similarly, pya.doubleClick(), pya.tripleClick(), pya.rightClick()... with optional parameters
time.sleep(3)

# Similarly; pya.mouseDown(x=45, y=65), pya.mouseDown(button='right')

#Drag the mouse
pya.dragTo(900, 300, duration=3)
time.sleep(2)
#Similarly, pya.draRel(200, 200, duration=2)


#Scrolling the mouse
pya.scroll(20)      #+ve integer scrolls up
time.sleep(2)


#Getting screenshot
screenshot = pya.screenshot()
print(screenshot.getpixel((150,230)))       #Returns Color of the point in rgb tuple. No alpha value because screenshots are fully opaque


#Analyze screenshot
#print(pya.pixelMatchesColor(100,200,(83, 62, 64))) #Returns true or false if color matches

#Image recognition
#pya.locateOnScreen('image.png')
#pya.locateAllOnScreen('image.png')


#Controlling keypboard
time.sleep(5)
pya.click(pya.position()[0], pya.position()[1])
pya.typewrite("This is a test text", 0.2)
time.sleep(3)

#Key Names
#E.g ESC = 'esc
#ENTER = 'enter'
# use pya.KEYBOARD_KEYS to view list of all keypress
pya.typewrite(['ctrl', 'a', 'right'])       #Simulate typing, NOT CTRL + A + RIGHT ARROW
time.sleep(2)


#Pressing and releasing the keyboards
pya.keyDown('ctrl')
pya.press('a')
pya.keyUp('ctrl')
pya.click(button='right')
time.sleep(2)
pya.moveRel(3, 10)


#OnScreen()
#To check if XY coordinates are on the screen
pya.onScreen(0,-1)      #-1 is not on the screen, hence false

#Hotkey
pya.hotkey('ctrl', 'a')
time.sleep(2)
pya.hotkey('win', 'd')



