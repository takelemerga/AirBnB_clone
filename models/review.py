#!/usr/bin/python3
"""review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """define review class """
    place_id = ""
    user_id = ""
    text = ""
