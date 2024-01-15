#!/usr/bin/env python3
"""
module for BaseModel class that defines all common:
-attributes
-methods
for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    BaseModel class
    """
    def __init__(self, *args, **kwargs):  # pylint: disable=unused-argument
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            # models.storage.save() //commented out at task 5

    def __str__(self):
        """
        string representation of Object when object is printed
        "[<class name>] (<self.id>) <self.__dict__>"
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__) \
            # pylint: disable=consider-using-f-string

    def save(self):
        """
        updates the public instance attribute "updated_at"
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary
        containing all key/values of "__dict__" of the instance
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict
