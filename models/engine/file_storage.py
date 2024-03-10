#!/usr/bin/python3
"""file storage modules"""
import datetime
import json
import os


class FileStorage:

    """FileStorage class serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        k = type(obj).__name__
        FileStorage.__objects["{}.{}".format(k, obj.id)] = obj

    def save(self):
        """serializes __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes JSON file to __objects if exist"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def classes(self):
        """classes method returns dictionary of valid classes and their reference"""
        from models.base_model import BaseModel
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "User": User}
        return classes

    def attributes(self):
        """attributes method returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str}
        }
        return attributes
