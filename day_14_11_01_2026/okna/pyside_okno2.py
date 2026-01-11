import sys
from PySide6.QtWidgets import QApplication, QWidget, QStyleFactory

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # wypisanie dostepnych styli
    print("Style available:", QStyleFactory.keys())
    # Style available: ['macOS', 'Windows', 'Fusion']

    # zastosowanie stylu
    app.setStyle(QStyleFactory.create("Fusion"))

    window = QWidget()
    window.setWindowTitle("Demo z Fusion")
    window.resize(300, 200)
    window.show()

    sys.exit(app.exec())
