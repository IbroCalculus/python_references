import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


class UI(QWidget):
    current_count = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('partTwo.ui', self)

        self.lblCount.setText("0")
        self.btnAdd.clicked.connect(self.increment)

    def increment(self):
        self.current_count += 1
        self.lblCount.setText(str(self.current_count))


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
