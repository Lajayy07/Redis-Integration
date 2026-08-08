# ---------------------------------------------------------
# Name: Cora Germany
# Date: August 8, 2026
# Project: MongoDB GitHub Archive Group Project
# Purpose: Provide three features and one analytical task
#          using GitHub Archive data stored in MongoDB.
# ---------------------------------------------------------

from pymongo import MongoClient
from collections import Counter
import matplotlib.pyplot as plt


# Connect to the local MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Change these names if your group uses different names
db = client["github_archive"]
collection = db["events"]

# ---------------------------------------------------------
# Feature 1: Count GitHub Events by Type
# ---------------------------------------------------------
def count_events_by_type():

    # Empty list to hold the event types
    event_types = []

    # Retrieve the type field from each MongoDB document
    for document in collection.find({}, {"type": 1, "_id": 0}):

        event_type = document.get("type")

        # Only add the value if the type field exists
        if event_type:
            event_types.append(event_type)

    # Make sure data was found
    if len(event_types) == 0:
        print("\nNo GitHub event types were found.")
        return

    # Count how many times each event type appears
    event_counts = Counter(event_types)

    print("\nGitHub Event Totals")
    print("-------------------")

    # Display events from most common to least common
    for event_type, count in event_counts.most_common():
        print(event_type + ": " + str(count))


# ---------------------------------------------------------
# Feature 2: Find the Five Most Active Repositories
# ---------------------------------------------------------
def most_active_repositories():

    # Empty list to hold repository names
    repo_names = []

    # Retrieve the repo field from each document
    for document in collection.find({}, {"repo.name": 1, "_id": 0}):

        # Get the repo object
        repo = document.get("repo", {})

        # Get the repository name
        repo_name = repo.get("name")

        # Only add valid repository names
        if repo_name:
            repo_names.append(repo_name)

    # Make sure repository data was found
    if len(repo_names) == 0:
        print("\nNo repository names were found.")
        return

    # Count how many events belong to each repository
    repo_counts = Counter(repo_names)

    print("\nFive Most Active Repositories")
    print("-----------------------------")

    # Display only the five most common repositories
    number = 1

    for repo_name, count in repo_counts.most_common(5):
        print(
            str(number)
            + ". "
            + repo_name
            + " - "
            + str(count)
            + " events"
        )

        number += 1


# ---------------------------------------------------------
# Feature 3: Repository Name-Length Survey
# ---------------------------------------------------------
def repository_name_survey():

    # Use a set so each repository is counted only once
    repo_names = set()

    # Retrieve repository names from MongoDB
    for document in collection.find({}, {"repo.name": 1, "_id": 0}):

        repo = document.get("repo", {})
        repo_name = repo.get("name")

        # Add valid repository names to the set
        if repo_name:
            repo_names.add(repo_name)

    # Make sure repository names were found
    if len(repo_names) == 0:
        print("\nNo repository names were found.")
        return

    # Find the shortest repository name
    shortest_name = min(repo_names, key=len)

    # Find the longest repository name
    longest_name = max(repo_names, key=len)

    # Add the lengths of all repository names
    total_length = 0

    for repo_name in repo_names:
        total_length += len(repo_name)

    # Calculate the average
    average_length = total_length / len(repo_names)

    print("\nRepository Name-Length Survey")
    print("-----------------------------")

    print(
        "Shortest name: "
        + shortest_name
        + " ("
        + str(len(shortest_name))
        + " characters)"
    )

    print(
        "Longest name: "
        + longest_name
        + " ("
        + str(len(longest_name))
        + " characters)"
    )

    print(
        "Average repository-name length: "
        + str(round(average_length, 2))
        + " characters"
    )


# ---------------------------------------------------------
# Analytical Task: Find the Most Active GitHub Users
# and display the results in a bar chart
# ---------------------------------------------------------
def most_active_users():

    # Empty list to store GitHub usernames
    user_names = []

    # Retrieve the actor.login field from MongoDB
    for document in collection.find({}, {"actor.login": 1, "_id": 0}):

        actor = document.get("actor", {})
        user_name = actor.get("login")

        # Only use valid usernames
        if user_name:
            user_names.append(user_name)

    # Make sure user data was found
    if len(user_names) == 0:
        print("\nNo GitHub users were found.")
        return

    # Count how many events each user created
    user_counts = Counter(user_names)

    # Get the five most active users
    top_users = user_counts.most_common(5)

    print("\nFive Most Active GitHub Users")
    print("-----------------------------")

    number = 1

    for user_name, count in top_users:
        print(
            str(number)
            + ". "
            + user_name
            + " - "
            + str(count)
            + " events"
        )

        number += 1

    # Lists used for the bar chart
    names = []
    counts = []

    for user_name, count in top_users:
        names.append(user_name)
        counts.append(count)

    # Create the bar chart
    plt.figure(figsize=(9, 5))
    plt.bar(names, counts)

    # Add chart labels
    plt.title("Five Most Active GitHub Users")
    plt.xlabel("GitHub User")
    plt.ylabel("Number of Events")

    # Make usernames easier to read
    plt.xticks(rotation=45)

    # Keep labels from being cut off
    plt.tight_layout()

    # Display the chart
    plt.show()


    # ---------------------------------------------------------
# Feature Menu
# ---------------------------------------------------------
def feature_menu():

    while True:

        print("\nMongoDB GitHub Archive Features")
        print("--------------------------------")
        print("1. Count GitHub Events by Type")
        print("2. Find Most Active Repositories")
        print("3. Repository Name-Length Survey")
        print("4. Most Active GitHub Users")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            count_events_by_type()

        elif choice == "2":
            most_active_repositories()

        elif choice == "3":
            repository_name_survey()

        elif choice == "4":
            most_active_users()

        elif choice == "5":
            print("\nReturning to the main program.")
            break

        else:
            print("\nInvalid choice. Please enter 1 through 5.")


# Start the feature menu
feature_menu()