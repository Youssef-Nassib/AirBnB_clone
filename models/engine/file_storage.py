#!/usr/bin/python3
"""file storage modules"""
import datetime
import json


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
        objdict = FileStorage.__objects
        odict = {obj: objdict[obj].to_dict() for obj in objdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(odict, f)

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

    def classes(self):
        """Returns a dictionary of classe and its reference"""
        from models.base_model import BaseModel
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "User": User}
        return classes

    def attributes(self):
        """Returns the valid attribute and their type for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime}
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
        }
        return attributes
