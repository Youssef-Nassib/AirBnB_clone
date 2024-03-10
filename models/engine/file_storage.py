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
            dt = {k: value.to_dict() for k, value in FileStorage.__objects.items()}
            json.dump(dt, f)

    def reload(self):
        """deserializes JSON file to __objects if exist"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            objct_dict = json.load(f)
            objct_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in objct_dict.items()}
            FileStorage.__objects = objct_dict

    def classes(self):
        """classes method returns dictionary of valid classes and their reference"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "City": City,
                   "State": State,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
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
                      "last_name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "State":
                     {"name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
                     {"place_id": str,
                      "user_id": str,
                      "text": str}
        }
        return attributes
