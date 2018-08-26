"""Unit tests for ducksearch module."""
from unittest import TestCase, mock, main
import json
import ducksearch
import wordlist
from request_mock import mocked_requests_get


class TestDucksearch(TestCase):
    """Ducksearch unit test suite."""

    @mock.patch('ducksearch.requests.get', side_effect=mocked_requests_get)
    @mock.patch('ducksearch.redis_client.lrange', return_value=[])
    @mock.patch('ducksearch.redis_client.lpush')
    def test_word_list_search_result_size(self, mock_redis_lpush, mock_redis_lrange, mock_get):
        """Check the number results returned is the same as the wordlist size."""
        json_result = ducksearch.search_word_list()
        result = json.loads(json_result)
        self.assertEqual(len(result), wordlist.NUMBER_OF_WORDS)

    @mock.patch('ducksearch.requests.get', side_effect=mocked_requests_get)
    @mock.patch('ducksearch.redis_client.lrange', return_value=["a", "b", "c"])
    @mock.patch('ducksearch.redis_client.lpush')
    def test_no_request_sent_if_cached_value(self, mock_redis_lpush, mock_redis_lrange, mock_get):
        """Check no request is sent to duckduckgo if there is a cached value."""
        ducksearch.get_top_three_titles_json("something")
        mock_get.assert_not_called()

    @mock.patch('ducksearch.requests.get', side_effect=mocked_requests_get)
    @mock.patch('ducksearch.redis_client.lrange', return_value=[])
    @mock.patch('ducksearch.redis_client.lpush')
    def test_parse_result(self, mock_redis_lpush, mock_redis_lrange, mock_get):
        """Check parsed titles match expected value."""
        expected_value = [
            "This is a test ad",
            "Test - Wikipedia",
            "Test | Definition of Test by Merriam-Webster"
        ]
        result = ducksearch.get_top_three_titles("something")
        self.assertListEqual(result, expected_value)

    @mock.patch('ducksearch.requests.get', side_effect=mocked_requests_get)
    @mock.patch('ducksearch.redis_client.lrange', return_value=[])
    @mock.patch('ducksearch.redis_client.lpush')
    def test_cache_push(self, mock_redis_lpush, mock_redis_lrange, mock_get):
        """Check an attempt is made to cache value, if no cached value provided."""
        titles = [
            "This is a test ad",
            "Test - Wikipedia",
            "Test | Definition of Test by Merriam-Webster"
        ]
        search_term = "something"
        ducksearch.get_top_three_titles(search_term)
        mock_redis_lpush.assert_called_with(search_term, *titles)

    @mock.patch('ducksearch.requests.get', side_effect=mocked_requests_get)
    @mock.patch('ducksearch.redis_client.lrange', return_value=[])
    @mock.patch('ducksearch.redis_client.lpush')
    def test_valid_json(self, mock_redis_lpush, mock_redis_lrange, mock_get):
        """Check the result provided is valid json."""
        json_result = ducksearch.get_top_three_titles_json("something")
        try:
            json.loads(json_result)

        except ValueError:
            self.fail("get_top_three_titles_json return invalid json")



if __name__ == '__main__':
    main()
