g1 = [x for x in range(5)]  # list comprenhensions
print(g1)  # [0, 1, 2, 3, 4]
print(type(g1))  # <class 'list'>

generator_2 = (x for x in [1, 2, 3, 4, 5])  # To jest generator!!!
print(type(generator_2))  # <class 'generator'>
print(generator_2)  # <generator object <genexpr> at 0x1021f6380>
print(next(generator_2))  # 1
print(next(generator_2))  # 2
print(next(generator_2))  # 3
print(next(generator_2))  # 4
print(next(generator_2))  # 5


def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))

