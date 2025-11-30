# class Person:
#     def __init__(self, first_name, last_name, id):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.id = id
#
#
# p1 = Person("Jan", "Kowalski", 1)
# print(p1)  # <__main__.Person object at 0x102c3a270>

from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(self.last_name)


p2 = Person("Jan", 'Kowalski', 1)
print(p2)  # Person(first_name='Jan', last_name='Kowalski', id=1)

p3 = Person("Maciej", "Nowak", 2)
print(p3)  # Person(first_name='Maciej', last_name='Nowak', id=2)
