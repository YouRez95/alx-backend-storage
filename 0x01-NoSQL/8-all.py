#!/usr/bin/env python3
"""
  function
    list_all
"""


def list_all(mongo_collection):
    """
        function that lists all documents in a collection
    """
    result = mongo_collection.find()
    if not result:
        return []
    return result
