import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

"""  IF DONE WITHIN qt designer

QPushButton#btnStyled {
    background-color: #4CAF50; /* Green background */
    color: white; /* White text */
    border: none; /* No border */
    padding: 10px 20px; /* Padding around text */
    text-align: center; /* Center text */
    text-decoration: none; /* No underline */
    display: inline-block; /* Inline block */
    font-size: 16px; /* Text size */
    margin: 4px 2px; /* Margin around button */
    cursor: pointer; /* Pointer cursor on hover */
}
QPushButton#btnStyled:hover {
    background-color: #45a049; /* Darker green on hover */
}
"""


class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up layout and buttons
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create buttons
        self.btnStyled = QPushButton("Styled Button")
        self.btnNormal = QPushButton("Normal Button")

        # Add buttons to layout
        layout.addWidget(self.btnStyled)
        layout.addWidget(self.btnNormal)

        # Set styles for the buttons
        self.btnStyled.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                border: none; /* No border */
                padding: 10px 20px; /* Padding around text */
                text-align: center; /* Center text */
                text-decoration: none; /* No underline */
                display: inline-block; /* Inline block */
                font-size: 16px; /* Text size */
                margin: 4px 2px; /* Margin around button */
                cursor: pointer; /* Pointer cursor on hover */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
        """)

        # Button without specific styling
        self.btnNormal.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0; /* Light grey background */
                color: black; /* Black text */
                border: 1px solid #ccc; /* Light grey border */
                padding: 8px 16px; /* Padding around text */
                font-size: 14px; /* Text size */
            }
        """)


# Run the application
app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
