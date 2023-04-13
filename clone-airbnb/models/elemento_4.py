#!/usr/bin/python3

import json
from sys import argv
import uuid

class Filestorage:
    __objects = {}
    __file_path = "file_2.json"

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()
            
        return self.__objects
    
        
    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass

        """
        with open(self.__file_path, 'r') as f:
            self.__objects = json.load(f)
        """

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if kwargs:
        
        self.data = kwargs
        estorage.new(self)

    def save(self):
        estorage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        return obj_dict.copy()

estorage = Filestorage()
estorage.reload()
model = BaseModel()
model.save()
"""
print(estorage.all())
"""
