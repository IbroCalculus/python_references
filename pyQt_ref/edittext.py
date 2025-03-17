import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox


# QLineEdit
# Use echoMode property to set it as password or not

class UI(QWidget):
    current_count = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)

        self.btnSayHello.clicked.connect(self.sayHello)

    def sayHello(self):
        retrievedText = self.et_fName.text()
        self.lbl_display.setText(retrievedText)
        print(f"Hello {retrievedText}")


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()