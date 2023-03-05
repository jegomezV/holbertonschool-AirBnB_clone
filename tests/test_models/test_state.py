#!/usr/bin/python3
"""Unittest module for the class State
"""
import unittest
import datetime
import models
from models.state import State
import os


class TestState(unittest.TestCase):
    """methods of the test for class State
    """
    def test_documentation(self):
        """this checks all the documentation
        of all the methods of the class
        """
        self.assertIsNotNone(models.state.__doc__)
        self.assertIsNotNone(State.__doc__)

    def test_uniqueId(self):
        """this check if the instance
        that are created has a unique id
        """
        instance1 = State()
        instance2 = State()
        self.assertNotEqual(instance1, instance2)
        self.assertNotEqual(instance1.id, instance2.id)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/state.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/state.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/state.py', os.X_OK)
        self.assertTrue(exect)

    def test_typeData(self):
        """this method check the type of
        the atributes when created a instance
        """
        instance1 = State()
        self.assertIsInstance(instance1.created_at, datetime.datetime)
        self.assertIsInstance(instance1.updated_at, datetime.datetime)
        self.assertIsInstance(instance1.id, str)
        self.assertIsInstance(instance1, State)

if __name__ == '__main__':
    unittest.main()
