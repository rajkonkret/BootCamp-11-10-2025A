import random

# random - działania na liczbach losowych

# """Return random integer in range [a, b], including both end points.
print(random.randint(1, 100))  # int 52 od 1 do 100

print(random.randrange(1, 100))  # 94, int, od 0 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # 0.04727211807938381, float, od 0 do 0.9999999
print(random.random() * 8)  # 1.9207021073560595, float, od 0 do 7.9999999
