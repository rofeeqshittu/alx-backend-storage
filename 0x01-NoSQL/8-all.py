#!/usr/bin/env python3
""" Contains list_all function """


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: The pymongo collection object
    :return: A list of documents in the collection or empty list if no document
    """
    # Retrieve all doc using find()
    doc = mongo_collection.find()

    # Convert cursor to a list & return
    return list(doc)
