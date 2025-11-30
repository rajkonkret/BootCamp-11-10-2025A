class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_fuction(x: int, y: int) -> float:
    if not isinstance(x, int):
        raise MyTypeError("X must be integer")
    if not isinstance(y, int):
        raise MyTypeError("Y must be integer")
    if y == 0:
        raise MyValueError("y cannot be zero")

    return x / y


# my_fuction("A", 1)  # MyTypeError: X must be integer
try:
    result = my_fuction(4, 5)
    # result = my_fuction(4, 0)
    result = my_fuction(4, 0)
except MyValueError as e:
    print("Caught a MytypeError")
    print("Error code:", e.err_code)
except Exception as e:
    print("Error:", e)
else:
    print(f"Result is: {result}")
finally:
    print("Next")
# Result is: 0.8
# Next

# Caught a MytypeError
# Error code: 100
# Next