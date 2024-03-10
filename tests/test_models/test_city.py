#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_default_attributes(self):
        # Create an instance of City
        city = City()

        # Assert that the default values of 'state_id' and 'name' attributes are empty strings
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
