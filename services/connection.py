from pymongo import MongoClient

class Connection():

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.database = self.client['Army']
        self.collection = self.database['Soldiers']