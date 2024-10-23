#!/usr/bin/env python3
"""
A module for using Redis as a NoSQL data storage, implementing
call tracking, history logging, and caching functionalities.
"""

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """
    A decorator to count how many times a method is called in the Cache class.

    It increments the counter in Redis each time the decorated method
    is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        The wrapper function that increments the method call count
        and then invokes the actual method.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator to store the history of inputs and outputs for a method
    in Redis.

    It logs the input arguments and the output to separate lists in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        The wrapper function that logs inputs and outputs to Redis,
        executes the method, and then returns the result.
        """
        in_key = f"{method.__qualname__}:inputs"
        out_key = f"{method.__qualname__}:outputs"

        if isinstance(self._redis, redis.Redis):
            # Store input args as strings
            self._redis.rpush(in_key, str(args))

        output = method(self, *args, **kwargs)  # Call the original method

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)  # Store the output

        return output

    return wrapper


def replay(method: Callable) -> None:
    """
    Displays the history of calls made to a method in the Cache class.

    It retrieves and prints the number of times the method was called,
    along with the inputs and outputs for each call.
    """
    if method is None or not hasattr(method, '__self__'):
        return

    redis_store = getattr(method.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return

    method_name = method.__qualname__
    in_key = f"{method_name}:inputs"
    out_key = f"{method_name}:outputs"

    # Retrieve and print how many times the method was called
    call_count = int(redis_store.get(method_name) or 0)
    print(f"{method_name} was called {call_count} times:")

    # Retrieve input/output lists from Redis
    inputs = redis_store.lrange(in_key, 0, -1)
    outputs = redis_store.lrange(out_key, 0, -1)

    # Print input/output history
    for inp, outp in zip(inputs, outputs):
        print(f"{method_name}(*{inp.decode('utf-8')}) -> {
              outp.decode('utf-8')}")


class Cache:
    """
    A Redis-based cache class for storing and retrieving data.

    This class supports tracking call history and counting method invocations
    """
    def __init__(self) -> None:
        """
        Initializes the Redis client and clears any existing data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)  # Clear the Redis database

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis and returns a randomly generated key.

        The data can be of type string, bytes, integer, or float.
        """
        key = str(uuid.uuid4())  # Generate a random UUID key
        self._redis.set(key, data)  # Store data in Redis using the key
        return key

    def get(self, key: str, fn: Callable = None) ->
    Union[str, bytes, int, float]:
        """
        Retrieves data from Redis using the provided key.

        If a callable `fn` is provided, it converts the data before
        returning it.
        """
        data = self._redis.get(key)  # Fetch data from Redis

        if data is None:
            return None

        return fn(data) if fn else data  # Apply conversion if fxn is provided

    def get_str(self, key: str) -> str:
        """
        Retrieves a string from Redis, converting the result if necessary.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer from Redis, converting the result if necessary.
        """
        return self.get(key, lambda d: int(d))
