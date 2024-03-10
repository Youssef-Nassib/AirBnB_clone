#!/usr/bin/python3
"""module for creating user"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class for managing users objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
