#!/usr/bin/python3
"""
-> It tells the operating system which program to use to execute the file.

Module ->

-This module contains the FileStorage class.
"""
from models.base_model import BaseModel
import os.path as path
import json


class FileStorage:
    """
    FileStorage Class ->

    -This class allows us to open a dictionary with "all" thanks to its own method.
    It is also in charge of the serialization and deserialization of the created instances,
    which inherit the attributes of the "BaseModel" class in Json format.
    --------------------------------------------->

    °Instance methods:
        public:
            -all(self)
            -new()
            -save(self)
            -reload(self)
    °Instance class attributes:
        private:
            - __file_path
            - __objects
    """ 
    __file_path = "file.json"
    __objects = {}
    """
    -La cadena "file.json" se usa como nombre de archivo predeterminado
    para almacenar objetos serializados en formato JSON.
    El archivo es específico para la aplicación y permite identificar fácilmente los objetos almacenados.
    """
    def all(self):
        """
        -This method returns a dictionary containing all of
        the objects stored in the JSON file.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        -This method adds a new object to the dictionary of
        objects stored in the JSON file.
        """
        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        -This method loads the dictionary of objects from the JSON file.
        """
        dic = {}
        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """ 
        -Deserialize the file json
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
