#!/usr/bin/env python3
"""
    class
        Cache
"""

import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    @wraps(method)
    def fn(self, *args, **kwargs) -> Any:
        """increments the count for that key every time the method is called"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return fn


class Cache:
    """A Cache class for redis"""
    def __init__(self) -> None:
        """Initiate a redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
