#!/usr/bin/env python3
"""
    class
        Cashe
"""

import redis
import uuid
from typing import Union


class Cache:

    """A Cache class for redis"""

    def __init__(self) -> None:
        """Initiate a redis"""
        r = redis.Redis()
        r.flushdb()
        self._redis = r

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in the redis"""
        id = str(uuid.uuid1())
        self._redis.set(id, data)
        return id
