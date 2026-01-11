import sys
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton


class Calculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
