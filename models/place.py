#!/usr/bin/python3
"""
A Place module that inherit from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A Place  class
    """
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, city, user, amenities, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = city
        self.user_id = user
        self.amenity_ids = amenities
