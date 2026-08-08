"""
Name: Alex Wiley
Date: 2026-08-08
Description: Read and import GitHub Archive JSON data
"""

import json
from pymongo import MongoClient

def mongodb_connector():
    # Connect to MongoDB
    myClient = MongoClient("mongodb://localhost:27017/")

    # Create database and collection
    db = myClient["github_archive"]
    return db["Licenses"]

#Reads JSON formatted GitHub Archive data and stores records in MongoDB.
def load_json_data():

    myCollection = mongodb_connector()

    print("Importing data from GitHub Archive...")
    for line in open('mongodb_licenses.json', 'r'):
        dataSet = json.loads(line)
        # Insert data into MongoDB
        myCollection.insert_one(dataSet)

    print("Data import success...")