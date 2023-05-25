#!/usr/bin/python3
import os

env = os.environ.get("HBNB_ENV")
user = os.environ.get("HBNB_MYSQL_USER")
password = os.environ.get("HBNB_MYSQL_PWD")
host = os.environ.get("HBNB_MYSQL_HOST")
database = os.environ.get("HBNB_MYSQL_DB")
storage_type = os.environ.get("HBNB_TYPE_STORAGE")

if storage_type == "file":
    # Use FileStorage to store data
    pass
elif storage_type == "db":
    # Use DBStorage to store data in MySQL database
    print(f"Connecting to {database} database on {host} as user {user}...")
    # Use these variables to connect to the MySQL database
    # Do something with the database connection...
else:
    # Handle unsupported storage types here
    print(f"Unsupported storage type: {storage_type}")

"""
export HBNB_ENV=production
export HBNB_MYSQL_USER=username
export HBNB_MYSQL_PWD=password
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=database_name
export HBNB_TYPE_STORAGE=db
"""
