#!/usr/bin/python3
"""
A module for filestorage
"""
import json
import os
from models import base_model, user


class FileStorage:
    """
    Filestorage class
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        returns the objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Sets obj with key in objects
        """
        key = "{}.{}".format(obj.to_dict()["__class__"], obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes objects to the JSON file
        """
        obj = {}
        for key, val in self.__objects.items():
            obj[key] = val.to_dict()
        json_str = json.dumps(obj)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json_str)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_str = f.read()
            for key, val in json.loads(json_str).items():
                if "BaseModel" in key:
                    self.__objects[key] = base_model.BaseModel(**val)
                if "User" in key:
                    self.__objects[key] = user.User(**val)
