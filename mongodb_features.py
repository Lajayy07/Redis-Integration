"""
Name: Alex Wiley
Date: 2026-08-08
Description: Add features to interact with database

    Feature 1: Count total licenses in database by license name.
    Feature 2: Count unique users in the license collection.

"""

# Pull myCollection from main to run function on database
def license_count(myCollection):

    license_results = myCollection.aggregate([
        {
            # group by id for aggregeation
            "$group": {
                "_id": "$license", "count": {"$sum": 1}
            }
        },
        {
            # order by descending to show the highest volume first
            "$sort": {"count": -1}
        }
    ])
    print("\nLicense volume by type")
    print("=======================\n")

    total_licenses = 0

    for license in license_results:# Connect to MongoDB
        print(f"{license['_id']}: {license['count']}")
        total_licenses += license["count"]

    print("\n=======================\n")
    print(f"Sum of licenses: {total_licenses}")

# Pull myCollection from main to run function on database
def repo_owner_count(myCollection):

    owner_results = myCollection.aggregate([ 
        # Group by repo owner for aggregation
        {
            "$group": {
                    "_id": {
                        "$arrayElemAt": [{"$split": ["$repo_name", "/"]}, 0]
                    },
                    "count": {"$sum": 1}
            }    
        }
    ])

    owner_count = 0

    for owner in owner_results:
            owner_count += 1

    total_repos = myCollection.count_documents({})

    print(f"\nTotal unique repo owners: {owner_count}")
    print(f"Total row count: {total_repos}")