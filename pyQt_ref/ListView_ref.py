import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication, QListWidget, QPushButton, QMessageBox, QListWidgetItem


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Load the .ui file created with Qt Designer

        # Find the list widget and button
        self.listWidget1 = self.findChild(QListWidget, 'listWidget1')
        self.btnGetListviewItems = self.findChild(QPushButton, 'btnGetListviewItems')

        # Connect the button click event to the handler
        self.btnGetListviewItems.clicked.connect(self.get_listview_items)

        # Connect the itemClicked signal to the handler
        self.listWidget1.itemClicked.connect(self.item_clicked)

        # Optionally populate the list widget with some items for demonstration
        self.populate_list_widget()

    def populate_list_widget(self):
        # Add items to the list widget (for demonstration purposes)
        items = ["Item 1", "Item 2", "Item 3", "Item 4"]
        self.listWidget1.addItems(items)
        self.listWidget1.addItem("item 5")

    def get_listview_items(self):
        # Retrieve all items from the list widget
        items = [self.listWidget1.item(i).text() for i in range(self.listWidget1.count())]
        # Print and display the items in a message box
        items_str = '\n'.join(items)
        print(f"ListWidget items:\n{items_str}")
        QMessageBox.information(self, 'ListView Items', f"ListWidget contains:\n{items_str}")

    def item_clicked(self, item: QListWidgetItem):
        # Print the text of the clicked item
        print(f"Clicked item: {item.text()}")
        QMessageBox.information(self, 'Item Clicked', f"You clicked: {item.text()}")


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
