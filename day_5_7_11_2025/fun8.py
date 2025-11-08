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


def allparams_all(a, b, /, c=43, *args, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f'{args}')
    print(f'{kwargs}')


allparams_all(1, 2)  # a=1, b=2
allparams_all(1, 2, 3)  # c=3,
allparams_all(1, 2, c=3)  # c=3,
# c musi byc pozycyjnie, jeśli chce przekazac d
allparams_all(1, 2, 3, 5)  # (5,)
allparams_all(1, 2, 3, 5, 6, 7, 8, 11, 12, 14, 15, 100)  # (5, 6, 7, 8, 11, 12, 14, 15, 100)
# d musimy przekazac po nazwie bo jest po *args
allparams_all(1, 2, 3, 5, 6, 7, 8, 11, 12, 14, 15, 100, d=89)  # (5, 6, 7, 8, 11, 12, 14, 15, 100)
allparams_all(1, 2, 3, 5, 6, 7, 8, 11, 12, 14, 15, 100, d=89, e=1000, name="Radek")  # (5, 6, 7, 8, 11, 12, 14, 15, 100)
# {'e': 1000, 'name': 'Radek'}
# a trafi do kwargs
allparams_all(1, 2, 3, 5, 6, 7, 8, 11, 12, 14, 15, 100, d=89, e=1000, name="Radek",
              a=10)  # (5, 6, 7, 8, 11, 12, 14, 15, 100)
