from dataclasses import dataclass
import os
import pymongo

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    
    
env_variable = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_variable.mongo_db_url)    