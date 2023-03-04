#!/usr/bin/python3
"""
-> It tells the operating system which program to use to execute the file.

Module ->

This module contains the BaseModel class.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    '''
    BaseModel Class ->

    -Define all common attributes and methods of the classes.
    The BaseModel methods return the instance of itself,
    already with the instance attributes set,
    and then convert it to Json format.
    The final result would be an instance that prints,and stored in json format:
    "[<<class name>] (<instance.id>) <attr.dict>".
    --------------------------------------------->

    °Instance methods:
        Public:
            - save(self)
            - to_dict(self)
    °Special method:
        - __init__(self)
        - __str__(self)
    °Instance attributes:
        Public:
            - id
            - created_at
            - updated_at
    '''
    def __init__(self, *args, **kwargs):
        '''
        -The __init__ method instantiates a new object of the BaseModel class.
        It checks if any arguments are passed and sets the corresponding attributes.
        If no arguments are provided, it generates a new UUID,
        sets the created_at and updated_at attributes to the current date and time, respectively.
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        '''
        __str__ method ->

        -This method returns the instance created in string format:
        "[<<class name>] (<instance.id>) <attr.dict>".
        '''
        return "[{}] ({}) {} ".format(type(self).__name__, self.id, self.__dict__)

    def save(self) -> None:
        '''
        save() method ->

        -This method updates the date and time, and then formats it to Json.
        '''
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        '''
        to_dict() method ->

        -This method returns a dictionary representation of the instance.
        The dictionary includes all of the instance's attributes,
        as well as the class name, created_at, and updated_at attributes.
        The created_at and updated_at attributes are formatted as ISO 8601
        strings using the datetime.isoformat() method.
        '''
        dicts = self.__dict__.copy()
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()
        dicts["__class__"] = type(self).__name__
        return dicts
