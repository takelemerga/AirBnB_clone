#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """ drived class that inherits from BaseModel
        gives user informations
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
