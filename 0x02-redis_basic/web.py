#!/usr/bin/env python3
"""
 Module Implementing an expiring web cache & tracker.
"""
import redis
import requests
from typing import Callable

# Initialize a Redis client
redis_client = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL and caches it in Redis.
    Tracks how many times the URL is accessed.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage.
    """
    # Key for tracking access count
    access_count_key = f"count:{url}"
    # Key for caching the webpage content
    cache_key = f"cached:{url}"

    # Increment the access count for the URL
    redis_client.incr(access_count_key)

    # Try to get the cached content from Redis
    cached_content = redis_client.get(cache_key)
    if cached_content:
        # If cached content exists, return it (no need to fetch again)
        return cached_content.decode('utf-8')

    # Fetch the webpage content using the requests module
    response = requests.get(url)
    content = response.text

    # Cache the content in Redis with an expiration time of 10 seconds
    redis_client.setex(cache_key, 10, content)

    return content


# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"  # A URL to test slow response
    print(get_page(url))  # Fetch the page and print content
    # Check how many times the URL was accessed
    print(redis_client.get(f"count:{url}"))
