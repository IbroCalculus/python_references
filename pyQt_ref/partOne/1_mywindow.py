from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hello World!")
window.setGeometry(100, 100, 400, 300)      # x,y, width, height



window.show()
sys.exit(app.exec())