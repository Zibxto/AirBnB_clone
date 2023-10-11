#!/usr/bin/python3
"""
A module for filestorage
"""
import json
import os


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
        key = "{}.{}".format(obj["__classname__"], obj["id"])
        self.__objects[key] = obj

    def save(self):
        """
        serializes objects to the JSON file
        """
        json_str = json.dumps(self.__objects)

        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json_str)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_str = f.read()
            self.__objects = json.loads(json_str)
