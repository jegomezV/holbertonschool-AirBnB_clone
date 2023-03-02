#!/usr/bin/python3
"""Unittest module for the class State
"""
import unittest
import datetime
import models
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """methods of the test for class State
    """
    def test_documentation(self):
        """this checks all the documentation
        of all the methods of the class
        """
        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_uniqueId(self):
        """this check if the instance
        that are created has a unique id
        """
        instance1 = FileStorage()
        instance2 = FileStorage()
        self.assertNotEqual(instance1, instance2)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exect)

    def test_typeData(self):
        """this method check the type of
        the atributes when created a instance
        """
        instance1 = FileStorage()
        self.assertIsInstance(instance1, FileStorage)

if __name__ == '__main__':
    unittest.main()
