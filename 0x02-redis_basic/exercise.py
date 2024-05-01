#!/usr/bin/env python3
"""
    class
        Cashe
"""

import redis
import uuid


class Cache:

    """A Cache class for redis"""
    redis.Redis().flushdb()

    def __init__(self):
        """Initiate a redis"""
        self._redis = redis.Redis()

    def store(self, data):
        """Store the data in the redis"""
        id = str(uuid.uuid1())
        self._redis.set(id, data)
        return id
