#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient


def log_stats():
    """
    Prints stats about Nginx request logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Count total logs
    total_logs = logs_collection.count_documents({})

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: logs_collection.count_documents({"method": method}) for method in methods}

    # Count GET requests where path is /status
    status_check = logs_collection.count_documents({"method": "GET", "path": "/status"})

    # Display the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()

