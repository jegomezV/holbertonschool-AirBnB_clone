#!/usr/bin/python3
""" Module holds city class that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a City
    Args:
        state_id (str): The id of the state
        name (str): Name of the city
    """

    state_id = ""
    name = ""
