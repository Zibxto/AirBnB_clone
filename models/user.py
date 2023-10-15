#!/usr/bin/python3
"""
A User module that inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initial user attributes"""
        super().__init__(*args, **kwargs)
