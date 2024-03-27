#!/usr/bin/python3
"""File storage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ a abstract engine for storing.

    Attributes:
        __file_path (str): name of the file to store.
        __objects (dict):a dict ob objectes instaned.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """set new object and with object id"""
        namec = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(namec, obj.id)] = obj

    def save(self):
        """serialize the list of objects into json file."""
        tdict = FileStorage.__objects
        obktodict = {obj: tdict[obj].to_dict() for obj in tdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obktodict, f)

    def reload(self):
        """deserialize the json file to object if exist."""
        try:
            with open(FileStorage.__file_path) as f:
                objtodict = json.load(f)
                for o in objtodict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
