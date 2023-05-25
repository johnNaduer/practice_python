#!/usr/bin/python3

import json
import uuid
import models
from sys import argv
from os.path import isfile
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class basemodel:
    __tablename__ = 'base_model'
    id = Column(String(60), primary_key=True, nullable=False)

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)        
        """
        self.kwargs = kwargs
        """
        models.estorage.new(self)
