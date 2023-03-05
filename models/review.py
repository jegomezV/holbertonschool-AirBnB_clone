#!/usr/bin/python3
""" Module holds Review class that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represents a review
    Args:
        place_id (str): id of Place
        user_id (str): User id
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""
