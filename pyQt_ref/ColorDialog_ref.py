import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QColor

class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up layout and button
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create a button to open the color dialog
        self.btnColorDialog = QPushButton("Select a Color")
        self.btnColorDialog.clicked.connect(self.open_color_dialog)
        layout.addWidget(self.btnColorDialog)

    def open_color_dialog(self):
        # Open the color dialog
        color = QColorDialog.getColor()

        # Check if the color is valid (i.e., the user didn't cancel the dialog)
        if color.isValid():
            # Show the selected color in a message box or change the background
            QMessageBox.information(self, "Selected Color", f"Selected Color: {color.name()}")
            self.setStyleSheet(f"background-color: {color.name()};")
            self.btnColorDialog.setStyleSheet(f"color: {color.name()}; background-color: white;")

        else:
            QMessageBox.warning(self, "Cancelled", "No color selected")

# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
