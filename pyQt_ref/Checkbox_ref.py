import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QCheckBox

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Load the .ui file created with Qt Designer

        # Find the checkboxes and button
        self.cb_meat = self.findChild(QCheckBox, 'cb_meat')  # Checkbox for Meat
        self.cb_fish = self.findChild(QCheckBox, 'cb_fish')  # Checkbox for Fish
        self.cb_turkey = self.findChild(QCheckBox, 'cb_turkey')  # Checkbox for Turkey
        self.btnCheck = self.findChild(QWidget, 'btnCheck')  # Button for checking

        # Connect the button click event to the function
        self.btnCheck.clicked.connect(self.check_selections)

        # Connect the stateChanged signal of checkboxes to a listener function
        self.cb_meat.stateChanged.connect(self.check_state_changed)
        self.cb_fish.stateChanged.connect(self.check_state_changed)
        self.cb_turkey.stateChanged.connect(self.check_state_changed)

    def check_selections(self):
        # Prepare the message based on selected checkboxes
        selected_items = []

        if self.cb_meat.isChecked():
            selected_items.append("Meat")
        if self.cb_fish.isChecked():
            selected_items.append("Fish")
        if self.cb_turkey.isChecked():
            selected_items.append("Turkey")

        # If any item is selected, show the selection, otherwise show a message
        if selected_items:
            QMessageBox.information(self, 'Selection', f"You selected: {', '.join(selected_items)}")
        else:
            QMessageBox.information(self, 'Selection', "No items selected")

    def check_state_changed(self, state):
        # Get the checkbox sender (the checkbox whose state changed)
        sender = self.sender()

        # Check the actual state of the checkbox using isChecked()
        if sender.isChecked():
            print(f"{sender.objectName()} selected")
        else:
            print(f"{sender.objectName()} deselected")


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
