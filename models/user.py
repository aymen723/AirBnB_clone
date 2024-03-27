#!/usr/bin/python3
""" User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """entity User.

    Attributes:
        email (str): email User.
        password (str): password for user.
        first_name (str): first name for user.
        last_name (str): last name for user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
