"""
Name: Alex Wiley
Date: 2026-08-08
Description: Main program

"""

from mongodb_import_data import (load_json_data, mongodb_connector)
from mongodb_crud import (create_record, read_record, update_record, delete_record, delete_all_records)
from mongodb_features import (license_count, repo_owner_count)

def display_menu():

    conn = mongodb_connector()

    if conn is None:
        print("Program cannot continue with a successful connection to MongoDB...")
        return

    while True:

        print("\nMongoDB CRUD Menu")
        print("1 - Load GitHub Archive JSON Data")
        print("2 - Create Record")
        print("3 - Read Records")
        print("4 - Update Record")
        print("5 - Delete Record")
        print("6 - License Volumes")
        print("7 - Repo Owner Volumes")
        print("8 - Delete all data")
        print("9 - Exit")

        choice = input("Select option: ")

        if choice == "1":
            load_json_data()

        elif choice == "2":
            create_record(conn)

        elif choice == "3":
            read_record(conn)

        elif choice == "4":
            update_record(conn)

        elif choice == "5":
            delete_record(conn)

        elif choice == "6":
            license_count(conn)

        elif choice == "7":
            repo_owner_count(conn)

        elif choice == "8":
            delete_all_records(conn)

        elif choice == "9":
            print("Program ended.")
            break

        else:
            print("Invalid option.")


# Start application
if __name__ == "__main__":
    display_menu()
