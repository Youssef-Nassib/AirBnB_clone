#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_default_attributes(self):
        # Create an instance of State
        state = State()

        # Assert that the default value of 'name' attribute is an empty string
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
