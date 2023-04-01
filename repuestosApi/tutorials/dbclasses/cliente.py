import pymongo
import os

from tutorials.dbclasses.dbmongo import DbMongo

class ClienteCollection:

    def __init__(self):
        self.client, self.db = DbMongo.getDB()
        self.collection = "tutorials_client"
    
    def getOne(self, id):
        collection = self.db[self.collection]
        return collection.find_one({"id_nacional": id})