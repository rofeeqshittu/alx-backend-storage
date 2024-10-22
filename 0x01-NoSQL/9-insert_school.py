#!/usr/bin/env python3
""" Contains insert_school() function. """



def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection.

    @mongo_collection: The pymongo collection object
    @kwargs: The fields for the new document
    @return: The new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
