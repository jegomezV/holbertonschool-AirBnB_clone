#!/usr/bin/python3
""" Module holds State class that inherits from BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """ Representation of a state
    Args:
        name (str): Name of the state
    """

    name = ""
