#!/usr/bin/env python3
"""
This module provides a function that returns all students
sorted by their average score.
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score.
    Each returned document will have an additional field 'averageScore'.
    
    Args:
    mongo_collection: pymongo collection object.
    
    Returns:
    List of students with their average score.
    """
    pipeline = [
        {
            '$project': {
                'name': 1,
                'averageScore': { '$avg': '$topics.score' }
            }
        },
        {
            '$sort': { 'averageScore': -1 }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))


# For testing the function
def run():
    """Testing the top_students function."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students
    top_students_list = top_students(students_collection)
    
    for student in top_students_list:
        print("[{}] {} => {}".format(student.get('_id'), student.get('name'), student.get('averageScore')))


if __name__ == "__main__":
    run()

