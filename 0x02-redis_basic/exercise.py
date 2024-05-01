#!/usr/bin/env python3
"""
    class
        Cache
"""

import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        if value and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """convert the data back to the string format"""
        return self._redis.get(key)

    def get_int(self, key: str) -> int:
        """convert the data back to the integer format"""
        value = self._redis.get(key)
        return int(value)
