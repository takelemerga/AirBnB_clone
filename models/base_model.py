#!/usr/bin/python3
"""a module that defines parent class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """a parent class: that defines all common attribute/methods
       for other classes that inherit from it.
    """
    date_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """set initial values for attributes of the instance of
           BaseModel class when it will be created.
           Args:
            *args: Is not used
            **kwargs: instance attributes - each key is an attribute name.
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if (key == "created_at" or key == "updated_at"):
                    setattr(
                       self, key, datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif (key == "id"):
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel class"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """Return string representation of BaseModel class"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
          self.created_at and self.updated_at -
                   'datetime' class data type attributes and
                    this data type converted to String data type.
          __class__ as key and 'classname' as value -  added to identify
          the dictonary of which instance.

          Return: dictionary representation of 'self' object.
        """
        str_dictionary = self.__dict__.copy()
        str_dictionary.update({'__class__': self.__class__.__name__})
        str_dictionary['created_at'] = self.created_at.isoformat()
        str_dictionary['updated_at'] = self.updated_at.isoformat()
        return str_dictionary
