#!/usr/bin/python3
"""Test base model Class"""

import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class."""

    def setUp(self):
        """Create a BaseModel instance for testing."""
        self.model = BaseModel()

    def test_initialization(self):
        """Test that a new instance of BaseModel is initialized correctly."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)
        # Ensure created_at and updated_at are the same initially
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_save(self):
        """Test the save method updates updated_at."""
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)
        # Ensure updated_at is greater than created_at after saving
        self.assertGreater(self.model.updated_at, self.model.created_at)

    def test_to_dict(self):
        """Test the to_dict method returns a correct dictionary."""
        model_dict = self.model.to_dict()
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["id"], self.model.id)
        # Ensure created_at and updated_at are in ISO format
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())

    def test_str(self):
        """Test the string representation of the model."""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)
