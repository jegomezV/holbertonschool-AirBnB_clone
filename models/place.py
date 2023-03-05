#!/usr/bin/python3
""" Module holds Place class that inherits from BaseModel """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Represent a place
    Args:
        city_id (str): City id
        user_id (str): User id
        name (str): Name of the place
        description (str): Description of Place
        number_rooms (int): Number of rooms in the place
        number_bathrooms (int): Number of bathrooms in the place
        max_guest (int): Maximum number of guests of the place
        price_by_night (int): Price by night of the place
        latitude (float): Latitude of the place
        longitude (float): Longitude of the place
        amenity_ids (list): List of amenity ids
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
