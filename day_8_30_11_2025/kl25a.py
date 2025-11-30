class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)
print(v2)
# Vector(1, 2)
# Vector(3, 4)

# dodawanie wektorów
# TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
# po nadpisanieu metody __add__ wynik:
v3 = v1 + v2
print(v3)  # Vector(4, 6)
