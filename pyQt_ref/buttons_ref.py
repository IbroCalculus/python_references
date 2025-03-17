import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


"""
    def button_clicked(self):
    
        # Get the button that was clicked using sender()
        button = self.sender()

        # Check the objectName
        if button.objectName() == "btn1":
            print("Button 1 was clicked!")
        elif button.objectName() == "btn2":
            print("Button 2 was clicked!")
"""

class UI(QWidget):
    current_count = 0

    def __init__(self):
        super().__init__()
        # uic.loadUi('partTwo.ui', self)    Assume loaded a ui with a label and a button

        self.lblCount.setText("0")
        self.btnAdd.clicked.connect(self.increment)

    def increment(self):
        self.current_count += 1
        self.lblCount.setText(str(self.current_count))


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
