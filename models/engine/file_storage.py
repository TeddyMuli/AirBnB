#!/usr/bin/python3
"""
Contains the FileStorage class model


"""
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    # empty dictionary
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the `obj` with key <obj class name>.id
        """
        obj = self.__objects[f"{obj.__class__.__name__}.{obj.id}"]

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dict_store = {}
            for i, j in self.__objects:
                dict_store[i] = j.to_dict()
            json.dump(dict_store, f)
        
    def reload(self):
        """
        Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for object in json.load(f).values():
                    self.new(eval(object["__class__"])(**object))
        except FileNotFoundError:
            return
