#!/usr/bin/python3
"""
Defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    class for BaseModel
    """
    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        date_now = datetime.now()
        self.created_at = date_now
        self.updated_at = date_now

        if kwargs:
            for key in kwargs.keys():
                if key == "__classname__":
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, kwargs.get(key))
        storage.new(self.to_dict())

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        curr_dict = self.__dict__
        curr_dict['__classname__'] = __class__.__name__
        str_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        curr_dict['created_at'] = curr_dict['created_at'].strftime(str_fmt)
        curr_dict['updated_at'] = curr_dict['updated_at'].strftime(str_fmt)
        return curr_dict

    def __str__(self):
        """
        String representation
        """
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)
