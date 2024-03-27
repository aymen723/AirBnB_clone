#!/usr/bin/python3
""" City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """entity of a city.

    Attributes:
        state_id (str): stateId.
        name (str): name City.
    """

    state_id = ""
    name = ""
