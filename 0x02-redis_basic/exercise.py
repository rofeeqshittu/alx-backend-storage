#!/usr/bin/env python3
"""
    Module for exercise.py
"""
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class. """
    def __init__(self):
        """
        Initialize the Cache class.
        Create a Redis client instance and flush the db to start fresh.
        """
        self._redis = redis.Redis()  # Initialize Redis client
        self._redis.flushdb()  # Clear the db to start with a clean slate

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis and return a randomly generated key.
        The data can be of type str, bytes, int or float.
        """
        random_key = str(uuid.uuid4())  # Generate a unique random key
        # Store data in Redis using the random key
        self._redis.set(random_key, data)
        return random_key  # Return the random key to the user
