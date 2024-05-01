#!/usr/bin/env python3
"""
    class
        Cache
"""

import redis
import uuid
from typing import Union


class Cache:
    """A Cache class for redis"""
    def __init__(self) -> None:
        """Initiate a redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in the redis"""
        id = str(uuid.uuid1())
        self._redis.set(id, data)
        return id
