#!/usr/bin/python3
"""This module contains the BaseModel class"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines the base class for all objects in the application"""

    def __init__(self, *args, **kwargs):
        """Instantiates a new object"""
        if kwargs:
            for key, value in kwargs.items():
                if key not in ["__class__"]:
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute and saves the object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a dict with all
        keys/values of the instance
        """
        dicts = self.__dict__.copy()
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        dicts["__class__"] = type(self).__name__
        return dicts
