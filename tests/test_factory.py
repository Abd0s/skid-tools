import unittest
from unittest import mock
import io as _io
import config
from skidtools import sfactory
import skidtools
import re

class GenerateCredentialsTestCase(unittest.TestCase):

    
    def test_number(self):
        credentials = sfactory.generate_credentials("number")
        self.assertTrue(credentials['firstname'].isdigit())
        self.assertTrue(credentials['lastname'].isdigit())
        self.assertTrue(credentials['username'].isdigit())

        self.assertTrue(isinstance(credentials['firstname'], str))
        self.assertTrue(isinstance(credentials['lastname'], str))
        self.assertTrue(isinstance(credentials['username'], str))
        self.assertTrue(isinstance(credentials['email'], str))
        self.assertTrue(isinstance(credentials['password'], str))

    def test_letter(self):
        credentials = sfactory.generate_credentials("letter")
        self.assertTrue(credentials['firstname'].isalpha())
        self.assertTrue(credentials['lastname'].isalpha())
        self.assertTrue(credentials['username'].isalpha())

        self.assertTrue(isinstance(credentials['firstname'], str))
        self.assertTrue(isinstance(credentials['lastname'], str))
        self.assertTrue(isinstance(credentials['username'], str))
        self.assertTrue(isinstance(credentials['email'], str))
        self.assertTrue(isinstance(credentials['password'], str))

    def test_mix(self):
        credentials = sfactory.generate_credentials("mix")
        self.assertTrue(isinstance(credentials['firstname'], str))
        self.assertTrue(isinstance(credentials['lastname'], str))
        self.assertTrue(isinstance(credentials['username'], str))
        self.assertTrue(isinstance(credentials['email'], str))
        self.assertTrue(isinstance(credentials['password'], str))


    def test_prefix(self):
        credentials = sfactory.generate_credentials("mix", "test")
        self.assertTrue(credentials['username'].startswith("test"))
        self.assertTrue(credentials['email'].startswith("test"))

    def test_invalid_engine(self):
        with self.assertRaises(ValueError) as f:
            sfactory.generate_credentials("invalid_engine", "test")
            self.assertEqual(f.exception, "Invalid argument: engine")




if __name__ == '__main__':
    unittest.main()