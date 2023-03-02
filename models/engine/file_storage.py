# coding=utf-8
#!/usr/bin/python3
"""Module for Filestorage class
"""
from models.base_model import BaseModel
import os.path as path
import json


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
        """ deserialize the file json
        with load y and returns to make
        a update with all objects
        """
        filename = FileStorage.__file_path
        if path.exists(filename):
            with open(filename, "r") as f:
                load = json.load(f)
            for k, v in load.items():
                suma = eval(v["__class__"])(**v)
                FileStorage.__objects[k] = suma
