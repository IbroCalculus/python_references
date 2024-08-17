import pyqrcode as pqr
import png
import os, shutil

file_name = input("Enter the file name for your qrcode: ")
text = input("Enter the text or URL to generate a QR Code: ")

file_name_svg = f'{file_name}.svg'
file_name_png = f'{file_name}.png'

url = pqr.create(text)

url.svg(file_name_svg, 8)       #8 is the size, it can vary
url.png(file_name_png, 10)

#============ END    ==========