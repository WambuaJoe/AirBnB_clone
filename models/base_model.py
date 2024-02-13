#!/usr/bin/python3
"""Define a Base Class for all models
    in the AirBnB clone
"""
import uuid
from datetime import datetime


Class BaseModel:
    """BaseModel class - all other classes inherit
        from it
    """
    def __init__(self, *args, **kwargs):
        """constructor method that initializes attributes
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """return string representation of an instance"""
        cls = (str(type(self)).split('.')[-1].split('\'')[0])
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
    
    def save(self):
        """update public instance attr updated_at with
            current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):