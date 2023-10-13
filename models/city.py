#!/usr/bin/python3
"""
A City module that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A City class
    """
    state_id = ""
    name = ""

    def __init__(self, state, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = state
