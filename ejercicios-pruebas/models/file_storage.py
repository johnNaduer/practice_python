#!/usr/bin/python3

import json
import uuid
from sys import argv
from os.path import isfile


class basemodel:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.kwargs = kwargs
        estorage.new(self)

class filestorage:
    file_path = "file3.json"
    __objects = {}

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.kwargs
        self.save()

    def save(self):
        with open(self.file_path, "w", encoding='utf-8') as f:
            dato_convert_json = json.dumps(self.__objects, indent=4)
            f.write(dato_convert_json)

    def all(self, cls=None):
        if cls is None:
            return self.__objects
        else:
            objects_list = {}
            for key, value in self.__objects.items():
                if cls.__name__ == value['__class__']:
                    objects_list[key] = value
            return objects_list

    def delete(self, obj=None):
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def reload(self):
        if isfile(self.file_path):
            with open(self.file_path, "r", encoding='utf-8') as f:
                self.__objects = json.load(f)
        else:
            return


estorage = filestorage()
estorage.reload()

