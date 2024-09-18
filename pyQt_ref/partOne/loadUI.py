import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('partone.ui', self)


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
