"""
log stats
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    num_logs = logs.count_documents({})
    num_get = logs.count_documents({"method": "GET"})
    num_post = logs.count_documents({"method": "POST"})
    num_put = logs.count_documents({"method": "PUT"})
    num_patch = logs.count_documents({"method": "PATCH"})
    num_delete = logs.count_documents({"method": "DELETE"})
    num_get_status = logs.count_documents({"method": "GET", "path": "/status"})
    print("{} logs".format(num_logs))
    print("Methods:")
    print("\t method GET: {}".format(num_get))
    print("\t method POST: {}".format(num_post))
    print("\t method PUT: {}".format(num_put))
    print("\t method PATCH: {}".format(num_patch))
    print("\t method DELETE: {}".format(num_delete))
    print("{} status check".format(num_get_status))
