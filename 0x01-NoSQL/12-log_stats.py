#!/usr/bin/env python3
""" Contains log_stats() fxn. """
from pymongo import MongoClient


def log_stats():
    """
    Logs stats

    @return: No return
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

