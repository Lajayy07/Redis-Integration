# ------------------------------------------------------------
# Name: Cora Germany
# Date: August 2, 2026
# Assignment: Redis Database Structure For Redi integration Group Project
#
# Purpose:
# This file creates the Redis database structure used to store
# GitHub Archive events.
#
# Redis structures used:
#
# 1. Set
#    Key: github:event_ids
#    Purpose: Stores every unique GitHub event ID.
#
# 2. Hash
#    Key format: github:event:<event_id>
#    Purpose: Stores the information for one GitHub event.
#
# Hash fields:
#    id
#    type
#    actor
#    repository
#    created_at
# ------------------------------------------------------------

import redis

def redis_connector():
# Connect to the local Redis server.
    try:
        r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
        r.ping()
        print("Connected to Redis successfuly.")
        return r
    except redis.RedisError as error:
        print("Could not connect to Redis.")
        print("Make sure Redis is running.")
        print(f"Error: {error}")
        return None

# Redis key that stores all event IDs.
EVENT_ID_SET = "github:event_ids"


def make_event_key(event_id):
    """Create the Redis key for one GitHub event."""
    return "github:event:" + str(event_id)


def create_database_structure():
    """
    Create sample records to demonstrate the Redis structure.

    Redis does not save empty sets or empty hashes, so sample
    events are inserted to show how the structure is organized.
    """

    sample_events = [
        {
            "id": "1001",
            "type": "PushEvent",
            "actor": "student_user",
            "repository": "student_user/python-project",
            "created_at": "2026-08-02T14:30:00Z"
        },
        {
            "id": "1002",
            "type": "CreateEvent",
            "actor": "sample_user",
            "repository": "sample_user/redis-project",
            "created_at": "2026-08-02T15:00:00Z"
        }
    ]

    for event in sample_events:
        event_id = event["id"]
        key = make_event_key(event_id)

        # Store the event information in a Redis hash.
        r.hset(key, mapping=event)

        # Store the event ID in the Redis set.
        r.sadd(EVENT_ID_SET, event_id)

    print("Redis database structure was created successfully.")


def display_database_structure():
    """Display the keys and sample event information."""

    print("\nREDIS DATABASE STRUCTURE")
    print("------------------------")
    print("Set key:", EVENT_ID_SET)
    print("Event IDs:", r.smembers(EVENT_ID_SET))

    for event_id in sorted(r.smembers(EVENT_ID_SET)):
        key = make_event_key(event_id)
        print("\nHash key:", key)

        event = r.hgetall(key)

        for field, value in event.items():
            print(field + ":", value)


def main():
    """Connect to Redis, create the structure, and display it."""

    redis_connector()
    create_database_structure()
    display_database_structure()



if __name__ == "__main__":
    main()
