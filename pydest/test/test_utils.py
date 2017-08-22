import pytest

from pydest.utils import check_alphanumeric


class TestCheckAlphanumeric(object):

    def test_alphabets(self):
        check_alphanumeric('abc')


    def test_alphabets_numbers(self):
        check_alphanumeric('a7b3c1')


    def test_special_characters(self):
        assert pytest.raises(ValueError, check_alphanumeric, '/*@&#%@%')


    def test_alphabets_and_special_characters(self):
        assert pytest.raises(ValueError, check_alphanumeric, 'a/b\c!')
