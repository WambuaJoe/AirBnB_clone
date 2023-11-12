#!/usr/bin/python3
"""FilesStorage module"""
import json
from datetime import datetime
import os


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in object with key"""
        dict_key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[dict_key] = obj

    def save(self):
        """serialize object to JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            pyObj = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(pyObj, file)

    def classes(self):
        """return dict of valid classes with their references"""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
        """deserialize JSON file to object"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                obj_dict = {key: self.classes()
                [value["__class__"]](**value)
                for key, value in obj_dict.items}
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass
