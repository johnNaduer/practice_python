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
    __objetos = {}

    def new(self, obj):
        key = obj.id
        self.__objetos[key] = obj.kwargs
        self.save()

    def save(self):
        with open(self.file_path,"w", encoding = 'utf-8') as f:
            dato_convert_json = json.dumps(self.__objetos, indent=4)
            f.write(dato_convert_json)


    def all(self):
        return self.__objetos

    def reload(self):
        if isfile(self.file_path):
            with open(self.file_path,"r", encoding = 'utf-8') as f:
                self.__objetos = json.load(f)
        else:
            return

estorage = filestorage()
estorage.reload()
dato1 = {"nombre":argv[1], "apellido":argv[2], "edad":argv[3]}
datos = basemodel(**dato1)
