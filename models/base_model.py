#!/usr/bin/python3
"""BaseModel module"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """create a BaseModel class"""
    def __init__(self):
        """initialize parameters"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """print human-readable output"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """update current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """return key-value pairs of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['update_at'] = my_dict['update_at'].isoformat()
        return my_dict
