#!/usr/bin/python3
"""FileStorage module"""
import os
import json
import datetime


class FileStorage:
    """FilesStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return object dictionary"""
        return FileStorage.__object

    def new(self, obj):
        """set new object using key"""
        key = "{}.{}".\
            format(type(self).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize object to JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            pyObj = {key: value.to_dict for key, value in FileStorage.__objects.items()}
            json.dump(pyObj, file)

    def classes(self):
        """return dict of valid classes & their representation"""
        from models.base_model import BaseModel

        classes = {
            'BaseModel': BaseModel
        }

    def reload(self):
        """deserialize JSON file to python object ONLY if file is found"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
            obj_dict = json.load(file)
            obj_dict = {key: self.classes()[value['__class__']](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict