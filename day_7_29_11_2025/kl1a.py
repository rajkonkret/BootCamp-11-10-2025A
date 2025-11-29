import math


class MyFirstClass:
    """
    Klasa w Pythonie opisująca punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Metoda przesuwa punkt we wskazane miejsce
        :param x: nowy x punktu
        :param y: nowy y punktu
        :return:
        """
        self.x = x
        self.y = y

    # metody tostring
    def __str__(self):
        return f"({self.x, self.y})"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x1005f9550>
# po nadpisaniu __str__ -> ((0, 0))
print(ob.x)
print(ob.y)

ob.move(67, 90)
print(ob)  # ((67, 90))
