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
        key = type(obj).__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """serializes __objects to JSON file"""
        file_path = FileStorage.__file_path
        with open(file_path, "w", encoding="utf-8") as f:
            data = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """deserializes JSON file to __objects if exist"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
