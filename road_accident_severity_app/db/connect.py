from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb+srv://malpaniharshit:DICProjectPhase3@dicprojectdb.6df47.mongodb.net/')
    return client['Road_Accident_Severity']
