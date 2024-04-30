#!/usr/bin/env python3
"""
  function
    top_students
"""


def mySort(e):
    """
      sorting function
    """
    return e['averageScore']


def top_students(mongo_collection):
    """
      sorting student by average score
    """
    students = mongo_collection.find()
    result = []
    for student in students:
        result.append(student)
    for std in result:
        std['averageScore'] = 0
        for topic in std['topics']:
            std['averageScore'] = (std['averageScore'] + topic['score'])
        std['averageScore'] = std['averageScore'] / len(std['topics'])
    result.sort(key=mySort, reverse=True)
    return result
