from abc import abstractmethod, ABC


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by  # values = values + by

    @abstractmethod
    def drukuj(self):
        pass
