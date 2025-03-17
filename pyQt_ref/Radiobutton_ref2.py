import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QButtonGroup


# This is less redundant

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)

        # Find radio buttons
        self.rbtnRed = self.findChild(QWidget, 'rbtnRed')
        self.rbtnYellow = self.findChild(QWidget, 'rbtnYellow')
        self.rbtnGreen = self.findChild(QWidget, 'rbtnGreen')
        self.rbtnPython = self.findChild(QWidget, 'rbtnPython')
        self.rbtnJava = self.findChild(QWidget, 'rbtnJava')
        self.rbtnCpp = self.findChild(QWidget, 'rbtnCpp')

        # Group color radio buttons
        self.color_group = QButtonGroup(self)
        self.color_group.addButton(self.rbtnRed)
        self.color_group.addButton(self.rbtnYellow)
        self.color_group.addButton(self.rbtnGreen)

        # Group language radio buttons
        self.language_group = QButtonGroup(self)
        self.language_group.addButton(self.rbtnPython)
        self.language_group.addButton(self.rbtnJava)
        self.language_group.addButton(self.rbtnCpp)

        # Connect radio buttons to the same slot
        self.color_group.buttonToggled.connect(self.radio_selected)
        self.language_group.buttonToggled.connect(self.radio_selected)

    def radio_selected(self, button):
        # Ensure button is checked
        if button.isChecked():
            # Process selection based on the group
            if button in self.color_group.buttons():
                selected = f"Color: {button.text()}"
            elif button in self.language_group.buttons():
                selected = f"Language: {button.text()}"

            print(selected)
            QMessageBox.information(self, 'Selection', f'You selected {selected}')


# Run the app
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()