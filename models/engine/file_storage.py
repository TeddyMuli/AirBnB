#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and 
    deserializes JSON file to an instance"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in objects the obj with key"""
        obj = self.__objects[f"{obj.__class__.__name__}.{obj.id}"]

    def save(self):
        """serializes __objects to the JSON file 
        (path: __file_path)"""
        with open(self.__file_path, mode="w") as f:
            storage = {}
            for i, j in self.__objects.items():
                storage[i] = j.to_dict()
            json.dumps(storage, f)

    def reload(self):
        """Deserialize the JSON file to _-objects
        """
        if self.__file_path:
            with open(self.__file_path, encoding="utf-8") as f:
                for object in json.load(f).value():
                    self.new(eval(object["__class__"])(**object))