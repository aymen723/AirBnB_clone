#!/usr/bin/python3
""" Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """entity a review.

    Attributes:
        place_id (str): PlaceID.
        user_id (str): UserID.
        text (str): comment of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
