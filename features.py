"""

Name: Alex Wiley
Assignment: 1.6 Group Project - Redis Integration
Date: 2026-08-02

Added features

Description: 
This python program has additional features added to show analytics for the repo database.

    1. Displays top 10 watched repos 
    2. Counts the total unique repos in the database

"""

def top_ten_repos(r):

    print("Top 10 Most Watched Repositories")
    print("--------------------------------")

    repo_list = []

    keys = r.keys("repo:*")

    for key in keys:

        repo = r.hgetall(key)

        repo_list.append(
            (
                repo["repo_name"],
                int(repo["watch_count"])
            )
        )

    repo_list.sort(key=lambda x: x[1], reverse=True)

    for repo_name, watch_count in repo_list[:10]:
        print(f"{repo_name} - {watch_count}")

def unique_repos(r):
    print("Counting unique repositories...")

    repo_keys = r.keys("repo:*")

    total_repos = len(repo_keys)

    print("\nRepository Count")
    print("================")
    print(f"Total unique repositories: {total_repos}")