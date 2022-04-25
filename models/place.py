#!/usr/bin/python3
"""place class module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        gives overall information about the place
        Class Attributes: (guest or host) of the place
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms of the place
        number_bathrooms (int): number of bathrooms of the place
        max_guest (int): number of maximum guests in the place
        price_by_night (int): price of the place by night
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (str): amenities of the place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
