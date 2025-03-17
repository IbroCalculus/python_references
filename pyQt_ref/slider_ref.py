import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QSlider, QPushButton

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Load the .ui file created with Qt Designer

        # Find the slider and button
        self.horizontalSlider1 = self.findChild(QSlider, 'horizontalSlider1')
        self.btnGetSliderValue = self.findChild(QPushButton, 'btnGetSliderValue')

        # Connect the button click event to the handler
        self.btnGetSliderValue.clicked.connect(self.get_slider_value)

        # Optionally connect the slider’s valueChanged signal to a handler
        self.horizontalSlider1.valueChanged.connect(self.slider_value_changed)

    def slider_value_changed(self, value):
        # This method is called whenever the slider value changes
        print(f"Slider value changed to: {value}")

    def get_slider_value(self):
        # This method is called when the button is clicked
        slider_value = self.horizontalSlider1.value()
        print(f"Button clicked, Slider value: {slider_value}")
        QMessageBox.information(self, 'Slider Value', f"Current slider value is: {slider_value}")

# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
