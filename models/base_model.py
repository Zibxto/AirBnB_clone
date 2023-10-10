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
    def __init__(self):
        self.id = str(uuid.uuid4())
        date_now = datetime.now()
        self.created_at = date_now
        self.updated_at = date_now
    
    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values

        """
        curr_dict = self.__dict__
        curr_dict['__classname__'] = __class__.__name__
        curr_dict['created_at'] = curr_dict['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        curr_dict['updated_at'] = curr_dict['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        return curr_dict

    def __str__(self):
        """
        String representation
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)