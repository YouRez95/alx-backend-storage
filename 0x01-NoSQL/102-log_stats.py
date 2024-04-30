#!/usr/bin/env python3
"""
print log stats
"""

from pymongo import MongoClient

if __name__ == "__main__":
    """
      Python script that provides
      some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    num_logs = logs.count_documents({})
    print('{} logs'.format(num_logs))
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        num_method = logs.count_documents({"method": method})
        print('\tmethod {}: {}'.format(method, num_method))
    num_get_status = logs.count_documents({"method": "GET", "path": "/status"})
    print('{} status check'.format(num_get_status))
    pipeline = [
        {
            '$group': {
                '_id': '$ip',
                'num_requests': {'$sum': 1}
            },
        },
        {
            '$sort': {'num_requests': -1}
        },
        {
            '$limit': 10
        }
    ]
    print('IPs:')
    for log in logs.aggregate(pipeline):
        print('\t{}: {}'.format(log['_id'], log['num_requests']))
