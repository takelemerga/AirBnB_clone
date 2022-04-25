#!/usr/bin/python3
"""User class testing module """
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class test_User(TestBaseModel):
    """testing class User """

    def __init__(self, *args, **kwargs):
        """initializer """
        super().__init__(*args, **kwargs)
    obj = User()

    def test_user_attr_type(self):
        """testing data type of class User attribute data type """
        self.assertEqual(type(self.obj.first_name), str)
        self.assertEqual(type(self.obj.last_name), str)
        self.assertEqual(type(self.obj.email), str)
        self.assertEqual(type(self.obj.password), str)
