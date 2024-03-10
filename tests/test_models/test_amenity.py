#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_default_attributes(self):
        # Create an instance of Amenity
        amenity = Amenity()

        # Assert that the default value of 'name' attribute is an empty string
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
