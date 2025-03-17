import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox


class UI(QWidget):
    current_count = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)

        self.btnAdd.clicked.connect(self.performOperation)
        self.btnSubtract.clicked.connect(self.performOperation)
        self.btnMultiply.clicked.connect(self.performOperation)
        self.btnDivide.clicked.connect(self.performOperation)

        # ===== Group A ==========
        self.rbtnRed = self.findChild(QWidget, 'rbtnRed')
        self.rbtnYellow = self.findChild(QWidget, 'rbtnYellow')
        self.rbtnGreen = self.findChild(QWidget, 'rbtnGreen')

        # ===== Group B ==========
        self.rbtnPython = self.findChild(QWidget, 'rbtnPython')
        self.rbtnJava = self.findChild(QWidget, 'rbtnJava')
        self.rbtnCpp = self.findChild(QWidget, 'rbtnCpp')

        # ===== onSelected ==========
        self.rbtnRed.toggled.connect(self.radio_selected_color)
        self.rbtnYellow.toggled.connect(self.radio_selected_color)
        self.rbtnGreen.toggled.connect(self.radio_selected_color)

        self.rbtnPython.toggled.connect(self.radio_selected_programminglanguage)
        self.rbtnJava.toggled.connect(self.radio_selected_programminglanguage)
        self.rbtnCpp.toggled.connect(self.radio_selected_programminglanguage)

    def radio_selected_color(self):
        # Check which radio button is selected
        if self.rbtnRed.isChecked():
            print("Red selected")
            QMessageBox.information(self, 'Selection', 'You selected Red')
        elif self.rbtnYellow.isChecked():
            print("Yellow is selected")
            QMessageBox.information(self, 'Selection', 'You selected Yellow')
        elif self.rbtnGreen.isChecked():
            print("Green selected")
            QMessageBox.information(self, 'Selection', 'You selected Green')

    def radio_selected_programminglanguage(self):
        # Check which radio button is selected
        if self.rbtnPython.isChecked():
            print("Python selected")
            QMessageBox.information(self, 'Selection', 'You selected Python')
        elif self.rbtnJava.isChecked():
            print("Java is selected")
            QMessageBox.information(self, 'Selection', 'You selected Java')
        elif self.rbtnCpp.isChecked():
            print("C++ selected")
            QMessageBox.information(self, 'Selection', 'You selected C++')

    def performOperation(self):
        fNumValue = self.et_fNum.text()
        sNumValue = self.et_sNum.text()

        button = self.sender()

        if button.objectName() == "btnAdd":
            result = float(fNumValue) + float(sNumValue)
        if button.objectName() == "btnSubtract":
            result = float(fNumValue) - float(sNumValue)
        if button.objectName() == "btnMultiply":
            result = float(fNumValue) * float(sNumValue)
        if button.objectName() == "btnDivide":
            try:
                result = float(fNumValue) / float(sNumValue)
            except ZeroDivisionError:
                QMessageBox.information(self, "Error", "Cannot divide by zero")
                return 0
        self.lbl_display.setText(f"{result}")


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
