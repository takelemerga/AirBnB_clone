#!/usr/bin/python3
"""testing module """
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class test_Amenity(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """initializing instance """
        super().__init__(*args, **kwargs)
    obj = Amenity()

    def test_amenity_attr_type(self):
        """testing Amenity class attr data type """
        self.assertEqual(type(self.obj.name), str)
