#!/usr/bin/python3
import unittest
from models.user import User  # Importing the User class to be tested


class TestUser(unittest.TestCase):
    def setUp(self):
        """Setup method called before each test method"""
        self.user = User()  # Creating a User instance for testing

    def test_attributes_initialization(self):
        """Test case to ensure attributes are initialized correctly"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attributes_assignment(self):
        """Test case to ensure attributes can be assigned values"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_str_representation(self):
        """Test case to ensure str method returns the expected string"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        
        expected_str = "<User: email='test@example.com', password='password123', first_name='John', last_name='Doe'>"
        
        self.assertEqual(str(self.user), expected_str)

if __name__ == '__main__':
    unittest.main()
