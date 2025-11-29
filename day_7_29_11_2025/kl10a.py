from abc import abstractmethod, ABC


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by  # values = values + by

    @abstractmethod
    def drukuj(self):
        pass

    # pozwala ominąc brak przeciązania konstruktorów
    @classmethod
    def from_counter(cls, counter):
        # Counter(bc.values)
        # zwraca obiekt klasy Counter
        return cls(counter.values)


# TypeError: Can't instantiate abstract
# class Counter without an implementation for abstract method 'drukuj'
# c1 = Counter()


class NewCounter(Counter):
    """
    Licznik bez metody dukuj()
    """


# TypeError: Can't instantiate abstract class NewCounter without
# an implementation for abstract method 'drukuj'
# nc = NewCounter()

# musimy dziedziczyi i nadpisać metode abstrakcyjną
class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError(F"Wartość nie może być większa od: {self.MAX}")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje...", self.values)


bc1 = BoundedCounter()
bc1.drukuj()  # Drukuje... 0
bc1.increment()
bc1.drukuj()  # Drukuje... 1
bc1.increment(5)
bc1.drukuj()  # Drukuje... 6

# bc2 = BoundedCounter(101)  # ValueError: Wartość nie może być większa od: 100

bc2 = BoundedCounter(bc1.values)
bc2.drukuj()  # Drukuje... 6

bc3 = BoundedCounter.from_counter(bc2)
bc3.drukuj()  # Drukuje... 6
bc4 = bc2.from_counter(bc3)
bc4.drukuj()  # Drukuje... 6
