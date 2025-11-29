class MyClassCounter:
    counter = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        return cls.counter


print(MyClassCounter.increment_counter())
print(MyClassCounter.increment_counter())
print(MyClassCounter.increment_counter())
c = MyClassCounter()
print(c.increment_counter())  # 4
