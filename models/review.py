#!/usr/bin/python3
"""review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review objects"""

    place_id = ""
    user_id = ""
    text = ""
