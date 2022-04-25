#!/usr/bin/python3
"""testing module  """
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class test_Place(TestBaseModel):
    """testing class Place"""

    def __init__(self, *args, **kwargs):
        """initialize instance"""
        super().__init__(*args, **kwargs)
    obj = Place()

    def test_place_attr_types(self):
        """ testing Attributes data types """  # Test Scenario
        self.assertEqual(type(self.obj.city_id), str)  # TestCase
        self.assertEqual(type(self.obj.user_id), str)  # TestCase
        self.assertEqual(type(self.obj.name), str)
        self.assertEqual(type(self.obj.description), str)
        self.assertEqual(type(self.obj.number_rooms), int)
        self.assertEqual(type(self.obj.number_bathrooms), int)
        self.assertEqual(type(self.obj.max_guest), int)
        self.assertEqual(type(self.obj.price_by_night), int)
        self.assertEqual(type(self.obj.latitude), float)
        self.assertEqual(type(self.obj.latitude), float)
        self.assertEqual(type(self.obj.amenity_ids), list)
