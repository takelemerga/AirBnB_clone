#!/usr/bin/python3
""" testing module """
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class test_City(TestBaseModel):
    """testing city class"""

    def __init__(self, *args, **kwargs):
        """initialize instance"""
        super().__init__(*args, **kwargs)
    obj = City()

    def test_state_attr_types(self):
        """testing attribute datatype"""  # TestScenario
        self.assertEqual(type(self.obj.state_id), str)  # TestCase
        self.assertEqual(type(self.obj.name), str)
