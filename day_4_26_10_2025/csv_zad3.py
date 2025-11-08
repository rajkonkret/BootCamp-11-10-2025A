import pandas

#  pip install pandas

data = pandas.read_csv('dane/records_discount.csv', delimiter=";")
print(data)
#    sku    exp_date   price
# 0    1  2025-11-09  100.00
# 1    2  2025-11-08  200.00
# 2    3  2025-11-09   50.00
# 3    4  2025-11-08  149.99
# 4    5  2025-11-08   75.00

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='object')

print(data.values)
# [[1 '2025-11-09' 100.0]
#  [2 '2025-11-08' 200.0]
#  [3 '2025-11-09' 50.0]
#  [4 '2025-11-08' 149.99]
#  [5 '2025-11-08' 75.0]]

print(data.items)
# <bound method DataFrame.items of    sku    exp_date   price
# 0    1  2025-11-09  100.00
# 1    2  2025-11-08  200.00
# 2    3  2025-11-09   50.00
# 3    4  2025-11-08  149.99
# 4    5  2025-11-08   75.00>
