"""

Name: Alex Wiley
Assignment: 1.6 Group Project - Redis Integration
Date: 2026-08-02

Main Python program

Description: 
Create a Python application that can perform CRUD operations on a Redis database. The program should meet the following criteria:

Read JSON-formatted data from the GitHub Archive to store and retrieve information in a Redis database.
Perform basic CRUD operations (Create, Read, Update, and Delete) on the data within the database.
Allow a user to perform basic CRUD operations on the data within the database.

"""

from redis_database_structure import redis_connector
from import_data import import_repo
from CRUD_Redis import (create_repo, review_repo, update_repo, delete_repo, flush_db)
from features import (top_ten_repos, unique_repos)

# Present a display menu to the end user to understand what options are available
def display_menu():
    
    print("""
    =====================================================
                        Navigation Menu
    =====================================================
    1. Review existing repos
    2. Add a new repo
    3. Update an existing repo
    4. Delete a repo
    5. Delete all data in database
    6. Import repo data
    7. Review top 10 repos
    8. Display total unique repos in database
    9. Exit program
    """
    )
    print("Enter a valid number and press enter to navigate to your menu option:")

def main():
    r = redis_connector()

    if r is None: 
        return

    while True:
        display_menu()

        try:
            route = int(input("Route to: ").strip())

            if not 1 <= route <= 9:
                print("Enter a number between 1 and 9.")
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
            import_repo(r)
        elif route == 7:
            top_ten_repos(r)
        elif route == 8:
            unique_repos(r)
        elif route == 9:
            print("Exited program successfully")
            break
        else:
            print("Invalid selection")

# Handle imports accordingly and execute the intended program 
if __name__ == "__main__":
    main()