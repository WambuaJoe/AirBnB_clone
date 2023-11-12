#!/usr/bin/python3
"""BaseModel module"""
from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    """create a BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initialize parameters"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(
                         kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.strptime(
                         kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            storage.new(self)

    def __str__(self):
        """print human-readable output"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """update current datetime"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return key-value pairs of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['update_at'] = my_dict['update_at'].isoformat()
        return my_dict
