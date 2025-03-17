import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QInputDialog, QMessageBox


class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Layout and buttons
        layout = QVBoxLayout()
        self.setLayout(layout)

        # String input button
        self.btnTextInput = QPushButton("Get Text Input")
        self.btnTextInput.clicked.connect(self.get_text_input)
        layout.addWidget(self.btnTextInput)

        # Integer input button
        self.btnIntInput = QPushButton("Get Integer Input")
        self.btnIntInput.clicked.connect(self.get_int_input)
        layout.addWidget(self.btnIntInput)

        # Double input button
        self.btnDoubleInput = QPushButton("Get Double Input")
        self.btnDoubleInput.clicked.connect(self.get_double_input)
        layout.addWidget(self.btnDoubleInput)

        # Item selection input button
        self.btnItemInput = QPushButton("Get Item Input")
        self.btnItemInput.clicked.connect(self.get_item_input)
        layout.addWidget(self.btnItemInput)

    # Function for string input
    def get_text_input(self):
        text, ok = QInputDialog.getText(self, "Text Input", "Enter your name:")
        if ok:
            QMessageBox.information(self, "Input", f"Your name is: {text}")
        else:
            QMessageBox.warning(self, "Cancelled", "No input received")

    # Function for integer input
    def get_int_input(self):
        integer, ok = QInputDialog.getInt(self, "Integer Input", "Enter your age:", min=0, max=100)
        if ok:
            QMessageBox.information(self, "Input", f"Your age is: {integer}")

    # Function for double input
    def get_double_input(self):
        value, ok = QInputDialog.getDouble(self, "Double Input", "Enter a decimal number:", min=0, max=100)
        if ok:
            QMessageBox.information(self, "Input", f"Your input is: {value}")

    # Function for item selection input
    def get_item_input(self):
        items = ["Python", "C++", "Java", "JavaScript"]
        item, ok = QInputDialog.getItem(self, "Select Item", "Choose your favorite language:", items, 0, False)
        if ok:
            QMessageBox.information(self, "Input", f"You selected: {item}")


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
