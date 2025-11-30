from functools import singledispatch


@singledispatch
def process(x):
    print("Default:", x)


@process.register(int)
def _(x):
    print("Int:", x)


@process.register(str)
def _(x):
    print("Str:", x)


process(42)  # Int: 42
process("Hello")  # Str: Hello
process(56)  # Int: 56

process(True)  # Int: True
process((2, 3))  # Default: (2, 3)
