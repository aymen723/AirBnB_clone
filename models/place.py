#!/usr/bin/python3
""" Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """entity a place.

    Attributes:
        city_id (str):  CityID.
        user_id (str): UserID.
        name (str): name.
        description (str):  desc of the place.
        number_rooms (int): nbr of rooms for the place.
        number_bathrooms (int): nbr of bathrooms for the entity place.
        max_guest (int):  maximum number of guests of the place.
        price_by_night (int): price by night .
        latitude (float): latitude of the place.
        longitude (float): longitude of place.
        amenity_ids (list): id list of amenity.
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
