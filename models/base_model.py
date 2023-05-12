#!/usr/bin/python3
"""Class that defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """The constructor"""

        #from models import storage
        if not kwargs:
            self.id = str(uuid4)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Returns the string representation of the object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    #public instance methods
    def save(self):
        """Updates the public instance attribute updated at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance:"""
        object = self.__dict__.copy()
        object['__class__'] = self.__class__.__name__
        object['created_at'] = self.created_at.isoformat()
        object['updated_at'] = self.updated_at.isoformat()
        return object
    
