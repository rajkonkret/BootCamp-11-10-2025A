from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi

# https://cloud.mongodb.com/v2/668572f48dedef138343f205#/overview

# pip install pymongo[srv]==3.13
uri = ""

# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())  # unix/linux

try:
    client.admin.command('ping')
    print("Pinged your deployment. you succesfully connected to MongoDB")
except Exception as e:
    print("Error::", e)
# Pinged your deployment. you succesfully connected to MongoDB
#
# Process finished with exit code 0
