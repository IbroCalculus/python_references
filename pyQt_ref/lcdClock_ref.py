import sys
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtWidgets import QWidget, QApplication, QLCDNumber


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Load the .ui file created with Qt Designer

        # Find the QLCDNumber widget
        self.lcdClock = self.findChild(QLCDNumber, 'lcdClock')

        self.lcdClock.setStyleSheet("""
            color: white;
            background-color: black;
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
        """)

        # Set the number of digits on the QLCDNumber (for HH:MM:SS, you need 8 digits)
        self.lcdClock.setDigitCount(12)

        # Set up the QTimer to update the clock every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 ms (1 second)

        # Initial call to display the current time immediately
        self.update_time()

    def update_time(self):
        # Get the current time
        current_time = QTime.currentTime()

        # Format the time as HHMMSS (8 digits in total)
        time_string = f"{current_time.hour():02} : {current_time.minute():02} : {current_time.second():02}"

        # Display the time on the QLCDNumber widget
        self.lcdClock.display(time_string)


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
