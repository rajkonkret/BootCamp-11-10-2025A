import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget
)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("HBOX Layout")

layout = QHBoxLayout()

layout.addWidget(QPushButton('Lewy'))

window.setLayout(layout)

window.show()
sys.exit(app.exec())
