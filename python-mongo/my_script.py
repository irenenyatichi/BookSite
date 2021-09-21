import pymongo
from pymongo import MongoClient
from utils import get_db_handle

mongo_client = MongoClient('localhost', 27017)

host_info = mongo_client['HOST']
print ("host:", host_info)
