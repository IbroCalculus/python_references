import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('alert_window.ui', self)

        # Connect the button click to the function that shows the alert
        self.btnAlert.clicked.connect(self.show_alert)

    def show_alert(self):
        # Create a QMessageBox
        msg_box = QMessageBox()

        # Set the icon (optional, you can choose other icons like Information, Warning, etc.)
        msg_box.setIcon(QMessageBox.Icon.Information)   # Warning, Critical, Question.

        # Set the message content
        msg_box.setWindowTitle("Alert")
        msg_box.setText("This is an alert pop-up message.")
        msg_box.setInformativeText("Additional information can be displayed here.")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        # Display the pop-up
        msg_box.exec()


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
