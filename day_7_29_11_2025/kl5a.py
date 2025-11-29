# Stworzyć słownik, który ma metode do wyszukiwania najdłuższego klucza w słowniku
# longest_key()

class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:  # zwraca klucze
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


# print(len(None)) # TypeError: object of type 'NoneType' has no len()

art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 7
art['zen'] = 1
print(art)  # {'tomasz': 12, 'abraham': 7, 'zen': 1}
print(art.longest_key())  # abraham


class LongestDictMariusz(dict):
    def longest_key(self):
        return max(self.keys(), key=len)


art = LongestDictMariusz()
art['tomasz'] = 12
art['abraham'] = 7
art['zen'] = 1
print(art)  # {'tomasz': 12, 'abraham': 7, 'zen': 1}
print(art.longest_key())  # abraham
# {'tomasz': 12, 'abraham': 7, 'zen': 1}
# abraham

if art.longest_key() == "abraham":
    print("ok")  # ok

assert 'abraham' == art.longest_key()
# assert 'abraham1' == art.longest_key()  # AssertionError
assert 4 == 2 * 2
