# NB: Need python version 3.5-3.9 to use pip install pyqt6-tools. Doesn't support a higher version

# https://build-system.fman.io/qt-designer-download (Download windows standalone installer for Qt Designer)
# pip install PyQt6
# pip install pyqt6-tools (Installs qt designer)
# .venv\Lib\site-packages\qt6_applications\Qt\bin\designer.exe  (Locate it in explorer and launch to run the qt designer)


# NB: There are 2 ways of accessing and using qt designer for your project, either by:
# 1. pip install pyqt6-tools and  locate and run designer.exe in
# .venv\Lib\site-packages\qt6_applications\Qt\bin\designer.exe, OR
# 2. by installing its standalone application on windows, via: https://build-system.fman.io/qt-designer-download
# Option 2 is better because pip install pyqt6-tools only works for python version 3.5 - 3.9

# ====== CONVERT .ui file to .py file ========
# run command > pyuic6 -x partone.ui -o partone.py          (where partone.py is the file name to convert to)


"""
from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Hello World!")
window.setGeometry(100, 100, 400, 300)      # x,y, width, height


window.show()
sys.exit(app.exec())
"""