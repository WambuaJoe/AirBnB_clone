#!/usr/bin/python3
"""defines class to manage file storage for AirBnB clone"""
import json


class FileStorage:
    """manage storage of models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dict of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to json file"""
        with open(FileStorage.__file_path, 'w') as file:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Loads storage dictionary from json file"""
        from models.base_model import BaseModel
        # from models.user import User
        # from models.place import Place
        # from models.state import State
        # from models.city import City
        # from models.amenity import Amenity
        # from models.review import Review

        classes = {
            'BaseModel': BaseModel
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
