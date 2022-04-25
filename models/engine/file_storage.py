#!/usr/bin/python3
"""file storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and
        deserializes JSON file to instance
    """
    __file_path = "jsonfile.json"
    __objects = {}
    name_classes = {"BaseModel": BaseModel, "User": User,
                    "Place": Place, "State": State, "City": City,
                    "Amenity": Amenity, "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """ set in __objects the obj with key object's classname+id
           <obj classname>.id
           args: obj - class instance (object)
        """
        obj_class_name = type(obj).__name__
        FileStorage.__objects.update(
          {"{}.{}".format(obj_class_name, obj.id): obj})

    def save(self):
        """serializes __objects dictionary to JSON file"""

        with open(FileStorage.__file_path, mode="w") as a_file:
            dict_of_dict = {}
            for key, obj in FileStorage.__objects.items():
                dict_of_dict.update({key: obj.to_dict()})
            json.dump(dict_of_dict, a_file)
            # a_file.write(json.dumps(dict_of_dict))
            # dict_of_dict[key] = obj.to_dict()
            # json.dump(dict_of_dict, a_file)

    def reload(self):
        """
          deserializes JSON file to __objects dictionary.
           __objects = {"classname.id": dictionary of instance}
           pass dictionary of instance(__objects's value) to
           class instance initializer as **kwargs
        """

        try:
            with open(self.__file_path, mode="r") as a_file:
                objects = json.load(a_file)
            for key, val in objects.items():
                name = key.split(".")[0]
                class_name = FileStorage.name_classes.get(name)
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, class_name, ids):
        """
        delete - delete an instance from the storage

        Args:
            class_name (str): name of the class
            ids (str): id of the instance

        Returns:
            None

        """
        aux = "{}.{}".format(class_name, ids)
        FileStorage.__objects.pop(aux)
        self.save()
