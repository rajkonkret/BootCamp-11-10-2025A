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


class Validator:

    @staticmethod
    def is_int(value, name):
        if not isinstance(value, int):
            raise MyTypeError(f"{name} must be integer")

    @staticmethod
    def not_zero(value, name):
        if value == 0:
            raise MyValueError(f"{name} cannot be zero")


# def my_fuction(x: int, y: int) -> float:
#     if not isinstance(x, int):
#         raise MyTypeError("X must be integer")
#     if not isinstance(y, int):
#         raise MyTypeError("Y must be integer")
#     if y == 0:
#         raise MyValueError("y cannot be zero")
#
#     return x / y

def my_fuction(x: int, y: int) -> float:
    Validator.is_int(x, "x")
    Validator.is_int(y, "y")
    Validator.not_zero(y, "y")

    return x / y


# my_fuction("A", 1)  # MyTypeError: X must be integer
try:
    result = my_fuction(4, 5)
    # result = my_fuction(4, 0)
    # result = my_fuction("Q", 0)
    result = my_fuction(0, 4)
except MyValueError as e:
    print("Caught a MyValueError")
    print("Error code:", e.err_code)
except MyTypeError as e:
    print("Caught MyTypeError")
    print("Error code:", e.err_code)
except Exception as e:
    print("Error:", e)
else:
    print(f"Result is: {result}")
finally:
    print("Next")
# Result is: 0.8
# Next

# Caught a MyValueError
# Error code: 100
# Next

# Caught MyTypeError
# Error code: 200
# Next

# Result is: 0.0
# Next
