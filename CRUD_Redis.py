"""

Name: Alex Wiley
Assignment: 1.6 Group Project - Redis Integration
Date: 2026-08-02

CRUD operations

Description: 
Create a Python application that can perform CRUD operations on a Redis database. The program should meet the following criteria:

Perform basic CRUD operations (Create, Read, Update, and Delete) on the data within the database.
Allow a user to perform basic CRUD operations on the data within the database.

"""

# Create a new repostitory record
def create_repo(r):
    print("Creating a new repo...")

    # prompt the user for the repo name
    repo_name = input("Enter the repo name (ex: username/project)").strip()

    # handle null entries 
    if repo_name == "":
        print("Repo name cannot be blank...")
        return
    # define key identifier
    key = "repo:" + repo_name

    # handle existing keys
    if r.exists(key):
        print("This repo already exists....")
        return
    
    # Error handling for unexpected input given 
    try:
        # Ask end user for the watch count associated to their repo
        watch_count = int(input("Enter the watch count of the repo: ").strip())

        # handle for negative values
        if watch_count < 0:
            print("Count cannot be a negative number.")
            return
    # exception handling
    except ValueError:
        print("Watch count must be a valid whole number...")
        return

    # add the hash
    r.hset(key, mapping = {"repo_name": repo_name, "watch_count": watch_count})

    # Display successful entry added
    print(f"\nRepo {repo_name} created successfully with {watch_count} watches.")

# Flush the database and delete all data
def flush_db(r):
    print("Wiping the database...")
    verify = input("Are you sure you want to clear all data from this database? (Y/N)\n").strip().upper()

    if verify in ("Y", "YES"):
        decision = input("Last check, continue with clearing all data from this database? (Y/N)\n").strip().upper()
        if decision in ("Y", "YES"):
            r.flushdb()
            print("All data has been successfully removed from the database...")
            return
        elif decision in ("N", "NO"):
            print("Operation cancelled...")
        else:
            print("You did not enter a valid option...")
            return
    elif verify in ("N", "NO"):
        print("Operation cancelled...")
        return
    else:
        print("You did not enter a valid option...")
        return
    
# Read an existing record in the Sample_Repos data
def review_repo(r):
    print("Review an existing repo...")
    # prompt end user to provide the repo name to review
    repo_name = input("Enter the repo name: ").strip()
    # define the key
    key = "repo:" + repo_name
    # check if the repo exists
    if not r.exists(key):
        print("The repo you entered does not exist...")
        return 
    # pull the repo to review
    repo = r.hgetall(key) 
    # display repo information
    print("\nRepo information")
    print("===================")
    print("Repo Name:", repo["repo_name"])
    print("Watch Count:", repo["watch_count"])

# Update a record 
def update_repo(r):
    print("Updating an existing repo...")

    repo_name = input("Enter the repo name: ").strip()

    key = "repo:" + repo_name

    if not r.exists(key):
        print("This repo does not exist...")
        return

    repo = r.hgetall(key)

    print("\nCurrent Repo Information")
    print("=================================")
    print("repo Name:", repo["repo_name"])
    print("Watch Count:", repo["watch_count"])

    try:
        new_watch_count = int(input("Enter the new watch count: ").strip())

        if new_watch_count < 0:
            print("Watch count cannot be negative...")
            return

    except ValueError:
        print("Watch count must be a valid whole number...")
        return

    r.hset(key, "watch_count", new_watch_count)

    print(f"repo {repo_name} updated successfully!")


# Delete an existing repo record
def delete_repo(r):
    print("Deleting an existing repo...")

    repo_name = input("Enter the repo name: ").strip()

    key = "repo:" + repo_name

    if not r.exists(key):
        print("This repo does not exist...")
        return

    verify = input(f"Are you sure you want to delete {repo_name}? (Y/N): ").strip().upper()

    if verify in ("Y", "YES"):
        r.delete(key)
        print(f"Repo {repo_name} deleted successfully!")

    elif verify in ("N", "NO"):
        print("Delete operation cancelled...")

    else:
        print("You did not enter a valid option...")

# Present a display menu to the end user to understand what options are available
def display_menu():
    
    print("""
    =====================================================
                        Navigation Menu
    =====================================================
    1. Review existing set members
    2. Add a new set
    3. Update an existing set
    4. Delete a set
    5. Delete all data in database
    6. Exit program
    """
    )
    print("Enter a valid number and press enter to navigate to your menu option:")

def main():

    if r is None: 
        return

    while True:
        display_menu()

        try:
            route = int(input("Route to: ").strip())

            if not 1 <= route <= 6:
                print("Enter a number between 1 and 6.")
                continue

        except ValueError:
            print("Expected integer data type only.")
            continue 

        if route == 1:
            review_repo(r)
        elif route == 2:
            create_repo(r)
        elif route == 3:
            update_repo(r)
        elif route == 4:
            delete_repo(r)
        elif route == 5:
            flush_db(r)
        elif route == 6:
            print("Exited program successfully")
            break
        else:
            print("Invalid selection")

# Handle imports accordingly and execute the intended program 
if __name__ == "__main__":
    main()