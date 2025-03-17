import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QButtonGroup


# There are two groups of radiobuttons used in this example
# NB: Group radiobuttons by placing within QGroupBox, or do it programmatically
# NB: It isn't compulsory to group, the  self.rbtnRed.toggled.connect(self.radio_selected_color) will group

class UI(QWidget):
    current_count = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)

        # ===============
        self.rbtnRed = self.findChild(QWidget, 'rbtnRed')
        self.rbtnYellow = self.findChild(QWidget, 'rbtnYellow')
        self.rbtnGreen = self.findChild(QWidget, 'rbtnGreen')

        # ===============
        self.rbtnPython = self.findChild(QWidget, 'rbtnPython')
        self.rbtnJava = self.findChild(QWidget, 'rbtnJava')
        self.rbtnCpp = self.findChild(QWidget, 'rbtnCpp')

        # ============ (OPTIONAL) Programmatically group radio buttons =================
        # Create QButtonGroup for colors
        self.color_group = QButtonGroup(self)
        self.color_group.addButton(self.radioRed)
        self.color_group.addButton(self.radioYellow)
        self.color_group.addButton(self.radioGreen)

        # Create QButtonGroup for programming languages
        self.language_group = QButtonGroup(self)
        self.language_group.addButton(self.radioJava)
        self.language_group.addButton(self.radioPython)
        self.language_group.addButton(self.radioCpp)

        # ===== END OPTIONAL ==========

        # ===== onSelect color radiobuttons ==========
        self.rbtnRed.toggled.connect(self.radio_selected_color)
        self.rbtnYellow.toggled.connect(self.radio_selected_color)
        self.rbtnGreen.toggled.connect(self.radio_selected_color)

        # ===== onSelect programming language radiobuttons ==========
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


app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
