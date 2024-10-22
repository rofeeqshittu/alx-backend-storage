#!/usr/bin/env python3
"""
Module to provide statistics about Nginx logs stored in MongoDB.
Now includes top 10 most present IPs.
"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Prints stats about Nginx request logs, including top 10 IPs."""
    # Get the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")
    
    # Count for status check (method=GET and path=/status)
    status_check_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check_count} status check")
    
    # Aggregation to get top 10 most present IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    
    top_ips = nginx_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


def run():
    """Connect to MongoDB and print Nginx logs stats."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    print_nginx_request_logs(nginx_collection)


if __name__ == "__main__":
    run()

