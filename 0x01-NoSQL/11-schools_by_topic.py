#!/usr/bin/env python3
""" Contains schools_by_topic() fxn. """


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.

    @topic: The topic to search for.
    @return: A list of matching schools
    """
    return list(mongo_collection.find({"topics": topic}))
