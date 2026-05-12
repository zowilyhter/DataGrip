# test_datagripdb.py
"""
Tests for DataGripDB module.
"""

import unittest
from datagripdb import DataGripDB

class TestDataGripDB(unittest.TestCase):
    """Test cases for DataGripDB class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataGripDB()
        self.assertIsInstance(instance, DataGripDB)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataGripDB()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
