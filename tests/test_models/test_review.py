#!/usr/bin/python3
""" Review Clas testing module """
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class test_review(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ initializing insatnce"""
        super().__init__(*args, **kwargs)
    obj = Review()

    def test_place_attr_type(self):
        """testing attributes data types """
        self.assertEqual(type(self.obj.place_id), str)
        self.assertEqual(type(self.obj.user_id), str)
        self.assertEqual(type(self.obj.text), str)
