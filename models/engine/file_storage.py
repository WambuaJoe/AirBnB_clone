#!/usr/bin/python3
"""defines a class to manage file storage"""
import json


class FileStorage:
    """manages storage of models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return dict of current models in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """add new object to dict"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """save storage dict to json file"""
        with open(FileStorage.__file_path, 'w') as fileObj:
            temp = {}
            temp.update(FileStorage.__objects)

            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, fileObj)

    def reload(self):
        """load storage dict from json file"""
        from models.base_model import BaseModel

        classes = {
            'BaseModel': BaseModel,
        }

        try:
            temporary = {}
            with open(FileStorage.__file_path, 'r') as json_file:
                temporary = json.load(json_file)
                for key, value in temporary.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
