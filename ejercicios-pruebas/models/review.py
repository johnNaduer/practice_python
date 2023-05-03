#!/usr/bin/python3

from .file_storage import basemodel

class review(basemodel):
    """ A class representing a Review """
    place_id = ""
    user_id = ""
    text = ""
