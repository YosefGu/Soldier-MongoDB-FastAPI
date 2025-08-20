from pymongo import MongoClient
import os


class Connection():

    def __init__(self):
        self.client = MongoClient(
           host=os.getenv('MONGO_HOST'),
           user=os.getenv('MONGO_USER'),
           password=os.getenv('MONGO_PASSWORD'),
           authSource='admin'
        )
        self.db = self.client[os.getenv('MONGO_DATABASE'), 'default_db']
        self.collection = self.db[os.getenv('MONGO_COLLECTION'), 'default_collection']
