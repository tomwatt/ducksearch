"""Requests mock methods."""
import wordlist
import ducksearch

def mocked_requests_get(*args, **kwargs):
    """Will be used by the mock to replace requests.get."""
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    if args[0] == wordlist.WORD_LIST_URL:
        with open('test_list.txt', 'r') as words_file:
            data = words_file.read()
        return MockResponse(data, 200)

    if args[0] == ducksearch.SEARCH_URL:
        with open('test_duckduckgo_page.html', 'r') as html_file:
            data = html_file.read()
        return MockResponse(data, 200)


    return MockResponse(None, 404)
