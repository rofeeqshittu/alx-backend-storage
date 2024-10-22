# 0x01. NoSQL

## Overview
This project is designed to introduce you to NoSQL databases, with a focus on MongoDB. You will learn the basics of working with NoSQL databases, including the differences between NoSQL and SQL, how to query and manipulate data in MongoDB, and how to use Python with MongoDB via the PyMongo library.

## Concepts
- NoSQL databases
- MongoDB operations (CRUD)
- Using MongoDB with Python (PyMongo)
- Querying and updating MongoDB collections

## Tasks

| Task # | Filename                     | Description                                                                  |
|--------|-------------------------------|------------------------------------------------------------------------------|
| 0      | [0-list_databases](./0-list_databases) | Script that lists all databases in MongoDB.                                   |
| 1      | [1-use_or_create_database](./1-use_or_create_database) | Script that creates or uses the database `my_db`.                             |
| 2      | [2-insert](./2-insert)        | Script that inserts a document with the attribute `name: "Holberton school"` into the `school` collection. |
| 3      | [3-all](./3-all)              | Script that lists all documents in the `school` collection.                   |
| 4      | [4-match](./4-match)          | Script that lists all documents with `name="Holberton school"` in the `school` collection. |
| 5      | [5-count](./5-count)          | Script that displays the number of documents in the `school` collection.      |
| 6      | [6-update](./6-update)        | Script that adds a new attribute `address: "972 Mission street"` to documents with `name="Holberton school"`. |
| 7      | [7-delete](./7-delete)        | Script that deletes all documents with `name="Holberton school"` in the `school` collection. |
| 8      | [8-all.py](./8-all.py)        | Python function that lists all documents in a collection.                     |
| 9      | [9-insert_school.py](./9-insert_school.py) | Python function that inserts a new document in a collection based on keyword arguments. |
| 10     | [10-update_topics.py](./10-update_topics.py) | Python function that updates the topics of a school document based on the name. |
| 11          | [11-schools_by_topic.py](./11-schools_by_topic.py)                       | Python function that returns a list of schools having a specific topic.     |
| 12          | [12-log_stats.py](./12-log_stats.py)                                     | Python script that provides stats about Nginx logs stored in MongoDB.       |
| 13          | [100-find](./100-find)                                                   | Script that lists documents where name starts with "Holberton" in MongoDB.  |
| 14          | [101-students.py](./101-students.py)                                     | Python function that returns students sorted by average score in MongoDB.   |
| 15          | [102-log_stats.py](./102-log_stats.py)                                   | Improved log stats script to display the top 10 most present IPs.           |


## Setup Environment
### MongoDB Installation (Ubuntu 18.04)
Follow the steps to install MongoDB version 4.2:
```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org

