import sys
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget
)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Grid Layout")

layout = QGridLayout()

window.setLayout(layout)

window.show()
sys.exit(app.exec())
