#!/usr/bin/env python3
"""
Module that defines a class called `FileStorage`.
This class is responsible:
- for serializing instances of objects to a JSON file
- deserializing a JSON file back to instances
of objects.
"""
import json
from os.path import isfile


class FileStorage:
    """
    Serialize and Deserialize objects
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
        returns the dctionary "__object" Attribute
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets the `obj` in the `__objects` dictionary with the key `<obj class name>.id`.
        Args (obj):
            The `obj` parameter is an object that you want to store in the `__objects` dictionary.
        The object can be of any class. 
        The key for storing the object in the dictionary is generated using:
            the class name of the object (`obj.__class__.__name__`) and the `id`
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes "__objects" to the JSON file (path: "__file_path") if exists
        """
        final_dict = {}
        for key, value in FileStorage.__objects.items():
            final_dict[key] = value
        json_str = json.dumps(f"{final_dict}")
        f_name = FileStorage.__file_path
        with open(f_name, "w") as file: # pylint: disable=unspecified-encoding
            file.write(json_str)

    def reload(self):
        """
        deserializes the JSON file to "__objects"
        only if the JSON file (__file_path) exists  otherwise, do nothing.
        no exception should be raised
        """
        filename = FileStorage.__file_path
        if isfile(filename):
            with open(filename, "r") as file: # pylint: disable=unspecified-encoding
                json_string = file.read()
                load_obj = json.loads(json_string)               
                for key, value in load_obj.items():
                    class_name = value["__class__"]
                    obj = models.classes[class_name](**value)
                    self.__objects[key] = obj
