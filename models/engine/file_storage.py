#!/usr/bin/python3
import json
from os.path import exists

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}             # Dictionary to store all objects
    
    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            # Convert __objects to dictionary of dictionaries for JSON
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)
    
    def reload(self):
        """Deserializes the JSON file to __objects, if the file exists."""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                # Load data from JSON and recreate instances
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    # Dynamically recreate instance (e.g., BaseModel(**value))
                    self.__objects[key] = globals()[class_name](**value)

