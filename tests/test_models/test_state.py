#!/usr/bin/python3
"""state testing module """
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class test_state(TestBaseModel):
    """ test State Class """

    def __init__(self, *args, **kwargs):
        """initialize instance"""
        super().__init__(*args, **kwargs)
    obj = State()

    def test_state_attr_type(self):
        """testing State attribute type"""  # TestScenario
        self.assertEqual(type(self.obj.name), str)  # TestCase
