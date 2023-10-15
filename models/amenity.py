#!/usr/bin/python3
"""
A Amenity module that inherit from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    An Amenity class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
