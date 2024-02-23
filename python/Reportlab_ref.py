from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4



filename = "reportlab.pdf"
documentTitle = "Document Title"
title = "The Law of Grossmos"
subtitle = "Unto a journey to witness ..."
textLines = [
    'Line 1 on the law',
    'The second line dealing with the fountain of youth',
    'Line 3 about the firmament of Zulbacia'
]

image = "reportlab.jpg"

pdf = canvas.Canvas(filename, pagesize=A4)

# Get list of available reportlab inbuilt fonts we can use
for font in pdf.getAvailableFonts():
    print(font)

# Applying custom font (OPTIONAL)
pdfmetrics.registerFont(
    TTFont('abc', 'SakBunderan.ttf')
)
pdf.setFont('abc', 36)

pdf.setTitle(documentTitle)
# pdf.drawString(270,770,title)
pdf.drawCentredString(300,770,title)

pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subtitle)


pdf.setStrokeColorRGB(255, 0, 0)
pdf.line(30, 710, 550, 710)

text = pdf.beginText(40, 680)
text.setFont("Courier", 12)
text.setFillColor(colors.red)

for line in textLines:
    text.textLine(line)
pdf.drawText(text)


pdf.drawImage(image, 130, 400)

pdf.save()