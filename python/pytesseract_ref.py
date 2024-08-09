
# CHECK ALSO: FastAPI -> Projects -> OCR_Application -> db_main.py

# https://github.com/UB-Mannheim/tesseract/wiki     <- Install Tesseract on windows if not installed already
# pip install pytesseract
# https://pypi.org/project/pytesseract/

from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Simple image to string
print(pytesseract.image_to_string(Image.open('internet3.png')))
# print(pytesseract.image_to_string('test.png'))
