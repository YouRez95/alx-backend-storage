#!/usr/bin/env python3
"""
  function
    insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
      function that inserts a new document
      in a collection based on kwargs
    """
    result = mongo_collection.insert_one(kwargs).inserted_id
    return result
