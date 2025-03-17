import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFontDialog, QMessageBox


class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up layout and widgets
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create a label to display text with the selected font
        self.lblText = QLabel("Sample Text", self)
        layout.addWidget(self.lblText)

        # Create a button to open the font dialog
        self.btnFontDialog = QPushButton("Select Font")
        self.btnFontDialog.clicked.connect(self.open_font_dialog)
        layout.addWidget(self.btnFontDialog)

    def open_font_dialog(self):
        # Open the font dialog
        font, ok = QFontDialog.getFont()

        # Check if the user selected a font (i.e., didn't cancel)
        if ok:
            # Apply the selected font to the label
            self.lblText.setFont(font)
            self.lblText.setText(f"Sample Text in {font.family()}")

        else:
            # Inform the user that no font was selected
            QMessageBox.warning(self, "Cancelled", "No font selected")


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
