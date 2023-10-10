#!/usr/bin/python3
"""
Defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    class for BaseModel

    """
    def __init__(self, *args, **kwargs):

        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            date_now = datetime.now()
            self.created_at = date_now
            self.updated_at = date_now

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime

        """
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
