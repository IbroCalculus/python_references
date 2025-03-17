import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox


class UI(QWidget):
    current_count = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)

        self.lblCount.setText("0")
        self.btnAdd.clicked.connect(self.increment)

        # Add more items to the QComboBox programmatically if needed (OR Double click on QT Designer to edit)
        self.comboBox1.addItem("Option 1")
        self.comboBox1.addItem("Option 2")
        self.comboBox1.addItem("Option 3")

        # Connect the QComboBox selection change to a function
        self.comboBox1.currentIndexChanged.connect(self.selection_changed)

    def selection_changed(self):
        # Get the current text from the QComboBox
        selected_option = self.comboBox1.currentText()

        # Show a pop-up with the selected option
        QMessageBox.information(self, "Selection Changed", f"You selected: {selected_option}")



    def increment(self):
        self.current_count += 1
        self.lblCount.setText(str(self.current_count))


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()

