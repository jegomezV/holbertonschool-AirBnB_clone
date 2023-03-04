# coding=utf-8
#!/usr/bin/python3
"""Module for Filestorage class
"""
from models.base_model import BaseModel
import os.path as path
import json
import os


class FileStorage:
    """ serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return a dictionary with all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """this method create a key with the
        class and the id of the object"""
        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """this method serialize a dict and
        the write a in file .json
        """
        dic = {}
        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                deseria = json.load(file)
            for key, value in deseria.items():
                objd = eval(value["__class__"])(**value)
                FileStorage.__objects[key] = objd
