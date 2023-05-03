#!/usr/bin/python3

from .file_storage import basemodel

class user(basemodel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
