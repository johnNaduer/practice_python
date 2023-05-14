#!/usr/bin/python3

import os

env = os.getenv("HBNB_ENV")
user = os.getenv("HBNB_MYSQL_USER")
password = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
database = os.getenv("HBNB_MYSQL_DB")
storage_type = os.getenv("HBNB_TYPE_STORAGE")

if storage_type == "file":
    # Use FileStorage to store data
    print("es un archivo")
    pass
elif storage_type == "db":
    # Use DBStorage to store data in MySQL database
    print(f"Connecting to {database} database on {host} as user {user}...")
    # Use these variables to connect to the MySQL database
    # Do something with the database connection...
else:
    # Handle unsupported storage types here
    print(f"Unsupported storage type: {storage_type}")
