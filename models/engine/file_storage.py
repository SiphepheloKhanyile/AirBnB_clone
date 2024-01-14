#!/usr/bin/env python3
"""
Module that defines a class called `FileStorage`.
This class is responsible:
- for serializing instances of objects to a JSON file
- deserializing a JSON file back to instances
of objects.
"""
import json
from models.base_model import BaseModel
import models  # pylint: disable=unused-import
classes = {"BaseModel": BaseModel}


class FileStorage():
    """
    Serialize and Deserialize objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dctionary "__object" Attribute
        """
        return self.__objects

    def new(self, obj):
        """
         sets in `__objects` the `obj` with key `<obj class name>.id`
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        serializes `__objects` to the JSON file (path: `__file_path`)
        """
        final_dict = {}
        for ob in self.__objects:  # pylint: disable=C0206
            final_dict[ob] = self.__objects[ob].to_dict()

        with open(self.__file_path, "w") as file:  # pylint:disable=W1514
            json.dump(final_dict, file)

    def reload(self):
        """
        deserializes the JSON file to `__objects`
        only if the JSON file (`__file_path`) exists  otherwise, do nothing.
        no exception should be raised
        """
        try:
            with open(self.__file_path, "r") as file: \
                    # pylint: disable=W1514
                data = json.load(file)

            for key in data.keys():
                self.__objects[key] = \
                    classes[data[key]["__class__"]](**data[key])
        except FileNotFoundError:
            pass