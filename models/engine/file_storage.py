#!/usr/bin/python3
"""FileStorage module"""
from os import path
import json
import datetime


class FileStorage:
    """FilesStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return object dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """set new object using key"""
        key = "{}.{}".\
            format(type(self).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize object to JSON file"""
        save_to_dict = {}
        for key, value in FileStorage.__objects.items():
            save_to_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(save_to_dict))

    def classes(self):
        """return dict of valid classes & their representation"""
        from models.base_model import BaseModel

        classes = {
            'BaseModel': BaseModel
        }
        return classes

    def reload(self):
        """deserialize JSON file to python object ONLY if file is found"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    self.all()[key] = self.classes[value['__class__']](**value)
        else:
            pass
