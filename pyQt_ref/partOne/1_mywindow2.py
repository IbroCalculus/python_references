from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Hello Worlddddd!")
window.statusBar().showMessage("Hello World from statusbar showmessage!")
window.setGeometry(100, 100, 1200, 800)      # x,y, width, height
window.menuBar().addMenu("File")
window.menuBar().addMenu("Edit")
window.menuBar().addMenu("View")
window.menuBar().addMenu("About")


window.show()
sys.exit(app.exec())