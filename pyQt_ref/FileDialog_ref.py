import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel


class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create a button that opens the file picker dialog
        self.btnFilePicker = QPushButton('Select File')
        self.btnFilePicker.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.btnFilePicker)

        # Label to display the selected file path
        self.selectedFileLabel = QLabel('No file selected')
        layout.addWidget(self.selectedFileLabel)

    def open_file_dialog(self):
        # Open the file dialog and get the file path
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File', '', 'All Files (*);;Text Files (*.txt)')

        # If the user selects a file, display its path
        if file_path:
            self.selectedFileLabel.setText(f"Selected file: {file_path}")
        else:
            self.selectedFileLabel.setText("No file selected")


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
