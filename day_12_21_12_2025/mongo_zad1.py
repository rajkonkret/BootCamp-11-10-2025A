# MongoDB, popularnej, nierelacyjnej bazy danych NoSQL, która przechowuje dane w elastycznych,
# podobnych do JSON dokumentach,
# oferując skalowalność i wydajność dla dużych zbiorów danych, z pominięciem tradycyjnych tabel i wierszy
# https://www.ovhcloud.com/pl/learn/what-is-mongodb/

# docker pull mongo
# docker run --name mongodb1 -d -p 27017:27017 mongo

#  pip install --upgrade pymongo
import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017")

my_db = my_client['mydatabase']
my_col = my_db['customers']

print(my_db.list_collection_names())
