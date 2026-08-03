"""

Name: Alex Wiley
Assignment: 1.6 Group Project - Redis Integration
Date: 2026-08-02

Import data

Description: 
Create a Python application that can perform CRUD operations on a Redis database. The program should meet the following criteria:

Read JSON-formatted data from the GitHub Archive to store and retrieve information in a Redis database.

"""

import json

def import_repo(r):
    print("Importing repo data...")

    try:
        with open("Sample_Repos.json", "r", encoding="utf-8") as file:

            for line in file:
                data = json.loads(line)

                repo_name = data["repo_name"]
                watch_count = data["watch_count"]

                key = "repo:" + repo_name

                r.hset(key, mapping={"repo_name": repo_name, "watch_count": watch_count})

        print("Repo data imported successfully!")

    except FileNotFoundError:
        print("Sample_Repos.json could not be found.")

    except json.JSONDecodeError:
        print("An error occurred while reading the JSON data.")
 