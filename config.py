import pymongo 
import json
from bson import ObjectId

# connection string 
mongo_url = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongo_url)

#get the specific database from the db service 
db = client.get_database("UniteApparel2")




class JSONEncoder(json.JSONEncoder): 
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        
        return json.JSONEncoder.default(obj)

def json_parse(data): 
    return JSONEncoder().encode(data)