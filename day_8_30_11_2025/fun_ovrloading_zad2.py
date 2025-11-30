from multipledispatch import dispatch


#  pip install multipledispatch

class Printer:
    """
    Klasa Printer
    przeciążanie funkcji typem argumentu
    """

    @dispatch(str)
    def show(self, txt):
        print("Text:", txt.lower())

    @dispatch(int)
    def show(self, number):
        print("Liczba:", number)

    @dispatch(list)
    def show(self, arr):
        print("Lista:", arr)


p = Printer()
p.show("Hello")  # Text: hello
p.show(123)  # Liczba: 123
p.show([1, 2, 3])  # Lista: [1, 2, 3]
