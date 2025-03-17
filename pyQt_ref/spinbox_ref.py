import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QSpinBox, QPushButton


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Load the .ui file created with Qt Designer

        # Find the spinbox
        self.spinBox1 = self.findChild(QSpinBox, 'spinBox1')

        # Connect valueChanged signal of spinbox to the handler
        self.spinBox1.valueChanged.connect(self.spinbox_value_changed)

        # Connect the editingFinished signal of spinbox to the handler
        self.spinBox1.editingFinished.connect(self.spinbox_editing_finished)

        # Find the button
        self.btnSpinValue = self.findChild(QPushButton, 'btnSpinValue')

        # Connect the button click signal to retrieve the spinbox value
        self.btnSpinValue.clicked.connect(self.get_spinbox_value)

    def spinbox_value_changed(self, value):
        # This method is called whenever the spinbox value changes
        print(f"Spinbox value: {value}")

        # You can also retrieve the value from the spinbox object directly
        spin_value = self.spinBox1.value()
        print(f"Retrieved Spinbox Value: {spin_value}")

    def spinbox_editing_finished(self):
        # This method is called when the user finishes editing the spinbox
        spinbox_value = self.spinBox1.value()
        print(f"Editing finished, Spinbox value: {spinbox_value}")

    def get_spinbox_value(self):
        # This method is called when the button is clicked
        spinbox_value = self.spinBox1.value()
        print(f"Button clicked, Spinbox value: {spinbox_value}")


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
