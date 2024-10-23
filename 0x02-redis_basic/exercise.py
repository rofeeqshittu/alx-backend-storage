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

    def get(self, key: str, fn: Optional[Callable] = None) ->
    Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the provided key.
        If the optional callable 'fn' is provided, apply it to the
        retrieved data to convert it to the desired type. If the key does
        not exit, return None.
        """
        data = self._redis.get(key)  # Retrieve data from Redis
        if data is None:
            return None  # Return None if the  key does not exit
        if fn:
            return data  # Return the raw data if no conversion fxn is provide

    def get_str(self, key: str) -> Optional[str]:
        """
        Return a string from Redis by calling get & converting bytes to UTF-8
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_init(self, key: str) -> Optional[int]:
        """
        Retrieve an int from Redis by calling get & converting bytes to int.
        """
        return self.get(key, fn=int)
