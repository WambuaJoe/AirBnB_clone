#!/usr/bin/python3
"""BaseModel module"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    def __init__(self):
        """initialize attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print human-readable output"""
        # [<class name>] (<self.id>) <self.__dict__>
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return dict containing key-value pairs of instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
