#!/usr/bin/python3
""" Module holds class Amenity that inherits from BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Represents an amenity
    Args:
        name (str): The name of the amenity
    """

    name = ""
