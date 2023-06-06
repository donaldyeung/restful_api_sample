from pymongo import MongoClient
from bson.objectid import ObjectId

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.mydatabase
    return db