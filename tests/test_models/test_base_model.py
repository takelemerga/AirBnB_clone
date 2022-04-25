#!/usr/bin/python3

import unittest
from datetime import datetime
from models import base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)

    def setUp(self):
        """ """
        pass

    """def tearDown(self):
        try:
            os.remove('jsonfile.json')
        except:
            pass"""

    obj = BaseModel()

    def test_class_doc(self):
        """ test for class documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ test for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

    def testattr(self):
        """Test the attributes of BaseModel"""  # test scenario
        self.assertTrue(hasattr(self.obj, "created_at"))  # testcase
        self.assertTrue(hasattr(self.obj, "id"))  # testcase
        self.assertTrue(hasattr(self.obj, "updated_at"))
        self.assertTrue(type(self.obj.created_at) is datetime)
        self.assertEqual(type(self.obj.updated_at), datetime)
        self.assertTrue(type(self.obj.id) is str)
        self.assertFalse(type(self.obj.created_at) is str)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary"""  # testscenari
        dictio = self.obj.to_dict()
        self.assertTrue(type(dictio) is dict)  # testcase
        self.assertIn('__class__', dictio.keys())  # testcase
        self.assertIn('created_at', dictio.keys())  # testcase
        self.assertIn('updated_at', dictio.keys())
        self.assertIn('id', dictio.keys())
        self.assertEqual(dictio["__class__"], self.obj.__class__.__name__)
        self.assertTrue(type(dictio["created_at"]) is str)

    def test_dict_args(self):
        """testing when dictionary passed as argument"""  # test scenario
        dictionary = self.obj.to_dict()
        inst = BaseModel(**dictionary)
        self.assertFalse(self.obj is inst)  # testcase
        self.assertNotIn("__class__", inst.__dict__.keys())  # testcase
        self.assertNotEqual(inst.__dict__, dictionary)
        self.assertTrue(type(inst.created_at) is datetime)

    def test_save(self):
        """testing updated_at when save method called"""
        before = self.obj.to_dict()
        self.obj.save()
        after = self.obj.to_dict()
        self.assertNotEqual(before["updated_at"], after["updated_at"])
        self.assertEqual(before["created_at"], after["created_at"])
        self.assertEqual(before["id"], after["id"])

    def test_str(self):
        """Testing string representation of BaseModel class"""
        self.assertEqual(str(self.obj), '[{}] ({}) {}'.format(
            self.obj.__class__.__name__, self.obj.id, self.obj.__dict__))


if __name__ == "__main__":
    unittest.main()
