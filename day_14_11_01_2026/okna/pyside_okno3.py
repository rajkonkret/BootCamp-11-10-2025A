import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QLabel, QPushButton, QStyleFactory
)


# funkcja uruchamiana po nacisnięciu buttona
def show_text():
    pass


app = QApplication(sys.argv)

print(QStyleFactory.keys())  # ['macOS', 'Windows', 'Fusion']
app.setStyle("Fusion")

dialog = QWidget()
dialog.setWindowTitle("Okno z polem tekstowym")
dialog.setGeometry(100, 100, 300, 150)

# pole tekstowe
textbox = QLineEdit()
textbox.setPlaceholderText("Wpisz coś tutaj...")

# pole labelka
label = QLabel("Tekst pojawi się tutaj")

# button
button = QPushButton("Wyświetl tekst")

# podłaczenie przycisku z funkcją
button.clicked.connect(show_text)  # przekazujemy referencję
