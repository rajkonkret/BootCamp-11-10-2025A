# funkcja zagnieżdzona, funkcja wewnętrzna
# wykorzystywane w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():  # przypisze adres fun2
        print("To jest fun2")

    # fun2()  # uruchomienie funkcji
    print(fun2)  # <function fun1.<locals>.fun2 at 0x105a5d9e0>
    return fun2  # zwracamy adres funkcji


fun1()  # To jest fun1
func = fun1()
print(func)  # <function fun1.<locals>.fun2 at 0x104dd99e0>
print(type(func))  # <class 'function'>
func()  # uruchomienie funkcji, zawartej w zmiennej func
func()
# To jest fun2
# To jest fun2
