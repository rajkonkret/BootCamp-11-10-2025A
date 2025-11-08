def allparams(a, b, /, c, **kwargs):
    print(a, b, c)
    print(kwargs)


allparams(1, 2, 3)
# 1 2 3
# {}
allparams(1, 2, c=90)
# 1 2 90
# {}

# TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / argumenty po lwej stronie mogą być tylko wywołane pozycyjnie
# allparams(a=1, b=2, c=8)
# 1 2 8
# {}

allparams(1, 2, c=8, a=90)  # {'a': 90}
