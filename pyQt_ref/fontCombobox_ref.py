import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QFontComboBox, QLabel
from PyQt6.QtGui import QFont


class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI from Qt Designer file (test.ui)
        uic.loadUi('test.ui', self)

        # Find the QFontComboBox and QLabel from the UI
        self.fontComboBox = self.findChild(QFontComboBox, 'fontComboBox1')  # QFontComboBox in UI
        self.label1 = self.findChild(QLabel, 'label1')  # QLabel in UI

        # Set a default font for the label
        self.label1.setFont(QFont("Arial", 28))  # You can change the default font and size here

        # Connect the signal of the QFontComboBox to the handler method
        self.fontComboBox.currentFontChanged.connect(self.font_changed)

    def font_changed(self, font: QFont):
        # This method is triggered when the user selects a different font from QFontComboBox
        self.label1.setFont(font)  # Change the label's font to the selected font
        print(f"Selected Font: {font.family()}")  # Print selected font for debugging


# Initialize the application
app = QApplication(sys.argv)

# Create the UI window and show it
window = UI()
window.show()

# Execute the app
app.exec()
