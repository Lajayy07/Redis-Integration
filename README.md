# MongoDB GitHub Archive CRUD Application

## Description
This Python application reads JSON-formatted GitHub Archive data and stores it in MongoDB.

The program performs CRUD operations:

- Create: Add new repository records
- Read: Display repository information
- Update: Modify repository watch counts
- Delete: Remove repository records

## Technologies Used

- Python
- MongoDB
- PyMongo
- GitHub Archive JSON Dataset

## Python File

mongodb_crud.py

This file connects Python to MongoDB and performs database CRUD operations.

## How to Run

1. Start MongoDB server.
2. Install PyMongo:

# MongoDB GitHub Archive Features

## Contributor

Cora Germany

## Project Portion

Three Application Features and Analytical Task

## Purpose

The features portion focuses on creating three beginner-friendly features that analyze GitHub Archive data stored in MongoDB.
These features use Python to retrieve information from the database, count or compare values, and display useful results to the user.

The application uses GitHub Archive JSON data that has been imported into a MongoDB collection.

---

## Feature 1: Count GitHub Events by Type

This feature counts the different types of GitHub events stored in the MongoDB database.

Examples of event types include:

* PushEvent
* CreateEvent
* WatchEvent
* IssuesEvent
* PullRequestEvent

The program retrieves the `type` field from each MongoDB document and uses Python's `Counter` class to count how often each event type appears.

The results are displayed from the most common event type to the least common event type.

Example:

```text
GitHub Event Totals
-------------------
PushEvent: 125
CreateEvent: 74
WatchEvent: 53
IssuesEvent: 28
PullRequestEvent: 19
```

This feature demonstrates retrieving MongoDB data, working with document fields, counting repeated values, and displaying sorted results.

---

## Feature 2: Find the Most Active Repositories

This feature identifies the five repositories with the most activity in the selected GitHub Archive dataset.

The program retrieves the nested `repo.name` field from each MongoDB document. It then counts how many events are associated with each repository.

Example:

```text
Five Most Active Repositories
-----------------------------
1. developer/project-one - 48 events
2. company/project-two - 39 events
3. organization/project-three - 31 events
4. student/project-four - 26 events
5. developer/project-five - 21 events
```

A repository with a larger number of events had more activity during the time period represented by the selected GitHub Archive data. 
This does not necessarily mean the repository is one of the most popular repositories on all of GitHub.

This feature demonstrates working with nested MongoDB fields, counting values, sorting results, and displaying the top results.

---

## Feature 3: Repository Name-Length Survey

This feature examines the lengths of repository names stored in the database.

The program retrieves the `repo.name` field and determines:

* The shortest repository name
* The longest repository name
* The average repository-name length

Each unique repository is counted once for this survey.

Example:

```text
Repository Name-Length Survey
-----------------------------
Shortest name: user/app
Longest name: organization/advanced-software-development-project
Average repository-name length: 24.50 characters
```

Python's `len()`, `min()`, `max()`, and basic mathematical operations are used to calculate the results.

This feature demonstrates how text data retrieved from MongoDB can be converted into numerical information for analysis.

---

## Analytical Task: Most Active GitHub Users

The analytical task identifies the five users who generated the most GitHub events in the selected dataset.

The program retrieves the nested `actor.login` field from each MongoDB document and counts how often each username appears.

Example:

```text
Five Most Active GitHub Users
-----------------------------
1. user123 - 45 events
2. developerABC - 39 events
3. coder456 - 31 events
4. programmer1 - 27 events
5. githubuser7 - 22 events
```

The results can also be displayed in a bar chart using Matplotlib. The horizontal axis displays the GitHub usernames, and the vertical axis displays the number of events.

The analysis only represents activity found in the GitHub Archive file used for the project.

---

## Python Libraries

The following Python libraries are used for this portion of the project:

```python
from pymongo import MongoClient
from collections import Counter
import matplotlib.pyplot as plt
```

### PyMongo

PyMongo allows the Python application to connect to MongoDB and retrieve the GitHub Archive documents.

### Counter

`Counter` is part of Python's built-in `collections` library. It is used to count GitHub event types, repository activity, and user activity.

### Matplotlib

Matplotlib is used to create a bar chart for the analytical task.

---

## Dependencies

Install the required external libraries with:

```bash
python -m pip install pymongo matplotlib
```

Depending on the system, the following command may be required instead:

```bash
python3 -m pip install pymongo matplotlib
```

The `collections` library is included with Python and does not require a separate installation.

---

## MongoDB Connection

The program connects to a local MongoDB server using PyMongo.

Example:

```python
client = MongoClient("mongodb://localhost:27017/")
db = client["github_archive"]
collection = db["events"]
```

The database and collection names may need to be changed to match the names used by the group project.

---

## Running the Features

Run the Python program from the terminal:

```bash
python mongodb_features.py
```

or:

```bash
python3 mongodb_features.py
```

The user will see a menu similar to:

```text
MongoDB GitHub Archive Features
--------------------------------
1. Count GitHub Events by Type
2. Find Most Active Repositories
3. Repository Name-Length Survey
4. Most Active GitHub Users
5. Exit
```

The user enters the number for the feature they want to run.

---

## GitHub Archive Fields Used

The features use the following fields from the GitHub Archive documents:

| Field         | Purpose                                           |
| ------------- | ------------------------------------------------- |
| `type`        | Identifies the GitHub event type                  |
| `repo.name`   | Identifies the repository connected to an event   |
| `actor.login` | Identifies the GitHub user who generated an event |

---

## Notes

These features are intended to be combined with the group's main MongoDB application. The full group application will also contain Create, Read, Update, and Delete operations.

The feature functions were kept simple so the code is easy to understand, test, explain, and maintain.

If Matplotlib is unavailable in the school virtual lab, the three main features can still run without the chart. The analytical results can still be displayed as text until Matplotlib is available.

---
