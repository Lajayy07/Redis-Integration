"""
MongoDB CRUD Application
Author: Latice Jordan
Purpose: Read GitHub Archive JSON data and perform CRUD operations
         using MongoDB.
"""

def create_record(myCollection):
    """
    Creates a new repository record.
    """
    repo_name = input("Repository name (example: user_name/repo_name)").strip()
    license_name = input("License name: ").strip()

    if repo_name == "" or license_name == "":
        print("Your input cannot be blank...")
        return

    repo = {
        "repo_name": repo_name,
        "license": license_name
    }

    myCollection.insert_one(repo)

    print(f"Record {repo_name} created...")


def read_record(myCollection):
    """
    Reads and displays MongoDB records.
    """

    search = input("Repository name search by regex: (example: user_name/repo_name)").strip()

    if search == "":
        print("Your input cannot be blank...")
        return

    records = myCollection.find({
        "repo_name": {"$regex": search, "$options": "i"}
        })

    found = False

    for record in records:
        print(record)
        found = True

    if not found:
        print(f"No matching repo or username found with value {search}...")

def update_record(myCollection):
    """
    Updates repository license name.
    """

    repo_name = input("Enter repository name to update (example: user_name/repo_name): ").strip()

    new_license = input("Enter new license: ").strip()

    if repo_name == "" or new_license == "":
        print("Your input cannot be blank...")
        return

    result = myCollection.update_one(
        {"repo_name": repo_name},
        {
            "$set": {
                "license": new_license
            }
        }
    )

    if result.matched_count == 0:
        print("Repository does not exist...")
    else:
        print(f"Record {repo_name} updated.")


def delete_record(myCollection):
    """
    Deletes a repository record.
    """

    repo_name = input("Enter repository name to delete: ").strip()

    if repo_name == "":
        print("Your input cannot be blank...")
        return

    result = myCollection.delete_one(
        {"repo_name": repo_name}
    )

    if result.deleted_count == 0:
        print("Repository does not exist...")
    else:
        print(f"Repository {repo_name} deleted.")

# deletes all records in the collection
def delete_all_records(myCollection):

    confirm = input("Are you sure you want to continue? (Y/N): ").strip().upper()
    if confirm == "Y":

        final = input("Confirm again (Y/N): ").strip().upper()
        if final == "Y":
            result = myCollection.delete_many({})
            print(f"{result.deleted_count} records deleted...")
        elif final == "N":
            print("Operation cancelled...")
        else:
            print("Invalid selection...")

    elif confirm == "N":
        print("Operation cancelled...")
    else:
        print("Invalid selection...")
