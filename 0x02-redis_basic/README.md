# 0x02. Redis Basic

## Overview
This project focuses on using Redis for basic operations and caching in Python. Redis is an in-memory data structure store used as a database, cache, and message broker. The goal of this project is to familiarize yourself with basic Redis commands, handling data storage, retrieval, and advanced functionalities like expiring caches.

## Concepts
- **Redis Operations:** Learn to perform basic Redis operations such as storing strings, incrementing values, and working with lists.
- **Caching:** Implement a caching system to optimize data access.
- **Python Decorators:** Use decorators to track and log method calls and their input/output history.

## Tasks

| Task # | Filename | Description |
|--------|-----------|-------------|
| 0 | [exercise.py](./exercise.py) | **Writing strings to Redis**: Create a `Cache` class to store data in Redis with randomly generated keys. Implement the `store` method to handle string, bytes, int, and float data. |
| 1 | [exercise.py](./exercise.py) | **Reading from Redis and recovering original type**: Implement a `get` method that takes a key and an optional callable to convert data back to its original format. Add `get_str` and `get_int` methods. |
| 2 | [exercise.py](./exercise.py) | **Incrementing values**: Create a `count_calls` decorator to track how many times `store` has been called using the Redis `INCR` command. |
| 3 | [exercise.py](./exercise.py) | **Storing lists**: Create a `call_history` decorator that stores method inputs and outputs into two separate Redis lists using `rpush`. |
| 4 | [exercise.py](./exercise.py) | **Retrieving lists**: Implement a `replay` function that outputs the history of calls to a particular function, including input arguments and return values. |
| 5 | [web.py](./web.py) | **Implementing an expiring web cache and tracker**: Write a `get_page` function that fetches the HTML content of a URL and caches it in Redis for 10 seconds. Track the number of times a URL has been accessed. |

## Setup Environment
1. Install Redis on Ubuntu 18.04:
    ```bash
    sudo apt-get -y install redis-server
    ```
2. Install Redis Python Client:
    ```bash
    pip3 install redis
    ```
3. Configure Redis to bind to localhost:
    ```bash
    sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
    ```
4. Start Redis server:
    ```bash
    service redis-server start
    ```

## File Descriptions

### [exercise.py](./exercise.py)
This file contains the `Cache` class with methods for interacting with Redis. It includes:
- **store**: Saves data in Redis with a randomly generated key.
- **get**: Retrieves data from Redis and optionally converts it back to its original type.
- **count_calls**: Decorator to count how many times the `store` method is called.
- **call_history**: Decorator to track method input/output history in Redis.

### [web.py](./web.py)
Implements a web caching system using Redis. The `get_page` function retrieves HTML content from a URL, caches it for 10 seconds, and tracks the number of accesses to each URL.

## License
This project is part of the ALX Backend Storage curriculum. All rights reserved.

