#!/usr/bin/env python3
"""
module for BaseModel class that defines all common:
-attributes
-methods
for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class
    """
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        string representation of Object when object is printed
        "[<class name>] (<self.id>) <self.__dict__>"
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__})"

    def save(self):
        """
        updates the public instance attribute "updated_at"
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary
        containing all key/values of "__dict__" of the instance
        """
        inst_dict = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                continue
            inst_dict[key] = value

        inst_dict["__class__"] = type(self).__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict


if __name__ == "__main__":
    pass
