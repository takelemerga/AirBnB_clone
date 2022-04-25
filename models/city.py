#!/usr/bin/python3
"""City class module"""
from models.base_model import BaseModel


class City(BaseModel):
    """gives information about state id and name of city """
    state_id = ""
    name = ""
