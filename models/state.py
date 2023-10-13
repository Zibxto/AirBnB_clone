#!/usr/bin/python3
"""
A State module that inherit from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A State class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
