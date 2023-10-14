#!/usr/bin/python3
"""
A Review module that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A Review class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
