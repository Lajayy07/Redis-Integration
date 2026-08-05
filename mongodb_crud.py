"""
MongoDB CRUD Application
Author: Latice Jordan
Purpose: Read GitHub Archive JSON data and perform CRUD operations
         using MongoDB.
"""

import json
from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create database and collection
db = client["github_archive"]
collection = db["repositories"]


def load_json_data(file_path):
    """
    Reads JSON formatted GitHub Archive data
    and stores records in MongoDB.
    """

    with open(file_path, "r") as file:
        for line in file:
            record = json.loads(line)

            # Insert data into MongoDB
            collection.insert_one(record)

    print("JSON data successfully loaded into MongoDB.")


def create_record():
    """
    Creates a new repository record.
    """

    repo = {
        "repo_name": input("Repository name: "),
        "watch_count": input("Watch count: ")
    }

    collection.insert_one(repo)

    print("Record created.")


def read_records():
    """
    Reads and displays MongoDB records.
    """

    records = collection.find()

    for record in records:
        print(record)


def update_record():
    """
    Updates repository watch count.
    """

    name = input("Enter repository name to update: ")

    new_count = input("Enter new watch count: ")

    collection.update_one(
        {"repo_name": name},
        {
            "$set": {
                "watch_count": new_count
            }
        }
    )

    print("Record updated.")


def delete_record():
    """
    Deletes a repository record.
    """

    name = input("Enter repository name to delete: ")

    collection.delete_one(
        {"repo_name": name}
    )

    print("Record deleted.")


def menu():

    while True:

        print("\nMongoDB CRUD Menu")
        print("1. Load GitHub Archive JSON Data")
        print("2. Create Record")
        print("3. Read Records")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            load_json_data(
                "Sample_Repos.json"
            )

        elif choice == "2":
            create_record()

        elif choice == "3":
            read_records()

        elif choice == "4":
            update_record()

        elif choice == "5":
            delete_record()

        elif choice == "6":
            print("Program ended.")
            break

        else:
            print("Invalid option.")


# Start application
if __name__ == "__main__":
    menu()
