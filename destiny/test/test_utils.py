import unittest

from destiny.utils import check_alphanumeric


class TestCheckAlphanumeric(unittest.TestCase):
    """Unit test for check_alphanumeric()"""

    def test_alphabets(self):
        """Assert that a string of alphabets is alphanumeric"""
        try:
            check_alphanumeric('abc')
        except ValueError:
            self.fail("check_alphanumeric() raised ValueError unexpectedly")


    def test_alphabets_numbers(self):
        """Assert that a string of alphabets and numbers is alphanumeric"""
        try:
            check_alphanumeric('a7b3c1')
        except ValueError:
            self.fail("check_alphanumeric() raised ValueError unexpectedly")


    def test_special_characters(self):
        """Assert that a string of special characters is not alphanumeric"""
        self.assertRaises(ValueError, check_alphanumeric, '/*@&#%@%')


    def test_alphabets_and_special_characters(self):
        """Assert that a string with alphabets and special characters is not alphanumeric"""
        self.assertRaises(ValueError, check_alphanumeric, 'a/b\c)')


if __name__ == "__main__":
    unittest.main()
