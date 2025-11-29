d_python = {}
print(type(d_python))  # <class 'dict'>
print(d_python)  # {}


# print(d_python['name'])  # KeyError: 'name'

# __missing__ - wykonuje się , gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d1 = DefaultDict()
print(d1['name'])  # default


# zrobić słownik
# ktory, gdy nie ma klucza w słowniku
# dopisze ten klucz do słownika z wartością domyślną

class Autodict(dict):
    def __missing__(self, key):
        self[key] = 0  # dopisanie klucza do słownika
        return key


d2 = Autodict()
print(d2)  # {}
print(d2['name'])  # name
print(d2)  # {'name': 0}
d2['name'] = "Radek"
print(d2)  # {'name': 'Radek'}
print(d2['name'])  # Radek


# słownik, gdzie klucze są zapamiętane małą literę
# zwróci wartość dla klucza niezależnie czy podamy go mała czy dużą literą
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.casefold())
        return self.get(key)


d3 = CaseInsensitiveDict()
d3[1] = "Radek"
print(d3)  # {1: 'Radek'}
print(d3[1])
print(d3[2])  # AttributeError: 'int' object has no attribute 'casefold'
