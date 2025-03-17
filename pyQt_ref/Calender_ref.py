import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QCalendarWidget
from PyQt6.QtCore import QDate


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Load the .ui file created in Qt Designer

        # Find the QCalendarWidget and button
        self.calendarWidget1 = self.findChild(QCalendarWidget, 'calendarWidget1')
        self.btnGetCalendarValue = self.findChild(QPushButton, 'btnGetCalendarValue')

        # Connect the button click event to the function
        self.btnGetCalendarValue.clicked.connect(self.get_selected_date)

        # Connect the date selection change signal to a handler
        self.calendarWidget1.selectionChanged.connect(self.date_selected)

    def date_selected(self):
        # Get the selected date from the calendar widget
        selected_date = self.calendarWidget1.selectedDate()
        print(f"Date selected: {selected_date.toString()}")

    def get_selected_date(self):
        # Get the selected date from the calendar widget on button click
        selected_date = self.calendarWidget1.selectedDate()
        print(f"Button clicked, selected date: {selected_date.toString('yyyy-MM-dd')}")


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
