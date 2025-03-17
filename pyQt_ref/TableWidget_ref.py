import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QPushButton, QTableWidgetItem, QMessageBox

class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Load the UI file designed in Qt Designer
        uic.loadUi('test.ui', self)

        # Find the QTableWidget and QPushButton from the UI
        self.tableWidget1 = self.findChild(QTableWidget, 'tableWidget1')  # Table widget
        self.btnGetTableContent = self.findChild(QPushButton, 'btnGetTableContent')  # Button for getting table content

        # Set the number of rows and columns in the table (optional)
        self.tableWidget1.setRowCount(4)  # You can adjust row count here
        self.tableWidget1.setColumnCount(3)  # You can adjust column count here

        # Connect the button click to the method for getting table content
        self.btnGetTableContent.clicked.connect(self.get_table_content)

        # Example: Add some data to the table
        self.add_data_to_table()

    def add_data_to_table(self):
        # Add sample data to the table
        data = [
            ["John", "Doe", "35"],
            ["Jane", "Smith", "28"],
            ["Alice", "Johnson", "30"],
            ["Bob", "Brown", "40"]
        ]

        # Populate the table with data
        for row, entry in enumerate(data):
            print(f"Row: {row}, Column: {entry}")
            for column, item in enumerate(entry):
                self.tableWidget1.setItem(row, column, QTableWidgetItem(item))

    def get_table_content(self):
        # Retrieve and display the content of the table
        rows = self.tableWidget1.rowCount()
        columns = self.tableWidget1.columnCount()

        table_data = []
        for row in range(rows):
            row_data = []
            for column in range(columns):
                item = self.tableWidget1.item(row, column)  # Get the QTableWidgetItem at (row, column)
                if item:  # Check if there's an item in the cell
                    row_data.append(item.text())
                else:
                    row_data.append('')  # If no item, append empty string
            table_data.append(row_data)

        # Show the table content in a message box or print it
        QMessageBox.information(self, 'Table Content', f"Table Data:\n{table_data}")
        print(table_data)  # Optionally, print the table data for debugging

# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
