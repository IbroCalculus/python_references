import pyqrcode as pqr
import png
import os, shutil

title = input("Enter a title for your qrcode: ")
text = input("What would you like the QR Code to say?: ")

file_name_svg = f'{title}.svg'
file_name_png = f'{title}.png'

url = pqr.create(text)

url.svg(file_name_svg, 8)       #8 is the size, it can vary
url.png(file_name_png, 10)

#============ END    ==========

#This part of the code is to move the generated qrcode files to another  location using the shutil module
path = r'C:\Users\Ibrahim Suleiman\Desktop'
shutil.move(f'{file_name_png}', r'C:\Users\Ibrahim Suleiman\Desktop')
shutil.move(f'{file_name_svg}', r'C:\Users\Ibrahim Suleiman\Desktop')