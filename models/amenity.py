#!/usr/bin/python3
""" Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """representation model of amenity.

    Attributes:
        name (str): the name.
    """

    name = ""
