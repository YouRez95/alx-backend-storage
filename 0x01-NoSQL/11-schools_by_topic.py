#!/usr/bin/env python3
"""
  function
    schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
      function that returns the list
      of school having a specific topic
    """
    result = mongo_collection.find({
        "topics": {
            '$all': [topic]
        }
    })
    return result
