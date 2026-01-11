import sys
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
import ast
import operator

# dozwolone operatory
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def safe_calc(expr: str):
    node = ast.parse(expr, mode="eval")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)

        if isinstance(n, ast.Constant):
            return n.value

        if isinstance(n, ast.BinOp):
            if type(n.op) not in OPERATORS:
                raise ValueError("Niedozwolony operator")
            return OPERATORS[type(n.op)](
                _eval(n.left),
                _eval(n.right)
            )

        if isinstance(n, ast.UnaryOp):
            if type(n.op) not in OPERATORS:
                raise ValueError("Niedozwolony operator")
            return OPERATORS[type(n.op)](_eval(n.operand))

        raise ValueError("Niedozwolone wyrażenie")

    return _eval(node)


class Calculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        # dodanie ikonki
        self.setWindowIcon(QIcon(QPixmap("calculator.png")))

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.result_felds = QLineEdit()
        self.grid.addWidget(self.result_felds, 0, 0, 1, 4)  # jeden wiersz, cztery kolumny

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("C", 5, 0)

        self.result_felds.setFocus()
        self.setLayout(self.grid)

    def create_button(self, text, row, column):
        button = QPushButton(text)
        button.clicked.connect(lambda: self.button_click(text))
        self.grid.addWidget(button, row, column)

    def button_click(self, text):
        if text == "=":
            self.calculate()
        elif text == "C":
            self.result_felds.setText("")
        else:
            self.result_felds.setText(self.result_felds.text() + text)

    def calculate(self):
        try:
            # result = eval(self.result_felds.text())  # wykona działnie, zwróci wynik, niebezpieczne
            result = safe_calc(self.result_felds.text())
            self.result_felds.setText(str(result))
        except:
            self.result_felds.setText("Error !!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
