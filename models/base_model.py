#!/usr/bin/python3
"""
Defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    class for BaseModel
    """
    def __init__(self, *args, **kwargs):
        """Initialization function"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, kwargs.get(key))
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        curr_dict = self.__dict__.copy()
        curr_dict['__class__'] = self.__class__.__name__
        curr_dict['created_at'] = self.created_at.isoformat()
        curr_dict['updated_at'] = self.updated_at.isoformat()
        return curr_dict

    def __str__(self):
        """
        String representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
