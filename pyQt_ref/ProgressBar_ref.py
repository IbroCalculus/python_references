import sys
import time

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Load the .ui file

        # Find the widgets by their object name in the .ui file
        self.progressBar1 = self.findChild(QWidget, 'progressBar1')
        self.btnStartProgress = self.findChild(QWidget, 'btnStartProgress')

        # Set up initial configuration for the progress bar
        self.progressBar1.setMinimum(0)  # Minimum value is 0%
        self.progressBar1.setMaximum(100)  # Maximum value is 100%

        # Connect the button click to the start progress method
        self.btnStartProgress.clicked.connect(self.start_progress)

    def start_progress(self):
        # Set progress values for demonstration
        for i in range(101):
            time.sleep(.1)
            self.progressBar1.setValue(i)  # Update progress value


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
