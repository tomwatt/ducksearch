"""Unit tests for wordlist module."""
from unittest import TestCase, mock, main
import wordlist
from request_mock import mocked_requests_get

class TestWordlist(TestCase):
    """Wordlist unit test suite."""

    @mock.patch('wordlist.requests.get', side_effect=mocked_requests_get)
    def test_word_list_size(self, mock_get):
        """Check the size of the list returned is the same as requested."""
        word_list = wordlist.get_word_list(20)
        self.assertEqual(len(word_list), 20)

    @mock.patch('wordlist.requests.get', side_effect=mocked_requests_get)
    def test_filter_criteria(self, mock_get):
        """Check all returned values match filter criteria."""
        word_list = wordlist.get_word_list(20)
        for word in word_list:
            self.assertTrue(word.isalpha())
            self.assertTrue(word[0].islower())

    @mock.patch('wordlist.requests.get', side_effect=mocked_requests_get)
    def test_no_empty_strings(self, mock_get):
        """Check there are no empty strings."""
        word_list = wordlist.get_word_list(20)
        for word in word_list:
            self.assertTrue(word)


if __name__ == '__main__':
    main()
