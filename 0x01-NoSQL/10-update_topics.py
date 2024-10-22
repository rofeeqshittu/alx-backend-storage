#!/usr/bin/env python3
""" Contains update_topics function. """


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document.

    @name: The name of the school to update
    @topics: The list of topics to set for the school
    """
    mongo_collection.update_many(
            {"name": name},  # The filter to find the document
            {"$set": {"topics": topics}}  # The update operation
            )
