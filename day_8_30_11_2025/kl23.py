class MyNumber:
    def __init__(self, value):
        self.value = value


num1 = MyNumber(5)
num2 = MyNumber(15)

# TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
# print(num1 < num2)
print(5 < 15)  # True

print(num1.value < num2.value)  # True


class MyNumber2:
    def __init__(self, value):
        self.value = value
