import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QDoubleSpinBox, QPushButton


# NB: There is also spin. Check spinbox_ref.py

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Load the .ui file created with Qt Designer

        # Find the QDoubleSpinBox and button
        self.doubleSpinBox1 = self.findChild(QDoubleSpinBox, 'doubleSpinBox1')
        self.btnDoubleSpinValue = self.findChild(QPushButton, 'btnDoubleSpinValue')

        # Connect valueChanged signal of QDoubleSpinBox to the handler
        self.doubleSpinBox1.valueChanged.connect(self.double_spinbox_value_changed)

        # Connect the button click signal to retrieve the double spinbox value
        self.btnDoubleSpinValue.clicked.connect(self.get_double_spinbox_value)

    def double_spinbox_value_changed(self, value):
        # This method is called whenever the double spinbox value changes
        print(f"Double Spinbox value: {value}")

        # You can also retrieve the value from the double spinbox object directly
        double_spin_value = self.doubleSpinBox1.value()
        print(f"Retrieved Double Spinbox Value: {double_spin_value}")

    def get_double_spinbox_value(self):
        # This method is called when the button is clicked
        double_spinbox_value = self.doubleSpinBox1.value()
        print(f"Button clicked, Double Spinbox value: {double_spinbox_value}")

# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
