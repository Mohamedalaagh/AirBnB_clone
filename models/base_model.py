#!/usr/bin/python3
"""base model Class"""

import uuid
import datetime


class BaseModel():
    """A base class model that provides common functionality for all models."""

    def __init__(self):
        """This initializes instance attribute
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the 'updated_at' timestamp to the current time."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dict representation of the instance for serialization."""
        dic = {}
        for key, value in self.__dict__.items():
            dic[key] = value
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
