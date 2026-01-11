import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget
)

app = QApplication()
window = QWidget()
window.setWindowTitle("HBOX Layout")

layout = QHBoxLayout()

window.setLayout(layout)

window.show()
sys.exit(app.exec())
