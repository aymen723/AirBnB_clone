#!/usr/bin/python3
""" BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the represenation entity of the airbnb project."""

    def __init__(self, *args, **kwargs):
        """constructor a new base model.

        Args:
            *args (any): nothing.
            **kwargs (dict): value of attribute.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """update the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return dict of basemodel instances.
        including the class and there values.
        """
        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict

    def __str__(self):
        """Return the string representation of class model."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
