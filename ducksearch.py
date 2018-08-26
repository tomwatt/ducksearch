"""Allows searching of particular terms on DuckDuckGo."""
import json
import requests
from lxml.html import document_fromstring
import redis
from wordlist import get_word_list

SEARCH_URL = "https://duckduckgo.com/html/"
RESULT_DIV_ID = "links"
RESULT_CLASS = "result__title"
TITLE_CLASS = "result__a"
REDIS_HOST = "redis"
REDIS_PORT = "6379"

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True)

def search_word_list():
    """
    Return top titles on duckduckgo for a random list of words.

    Retrieve a list of random words, search each on duckduckgo and
    return the top three titles, as json.

    Returns:
        json of the form
        {
            "flower": ["title 1", "title 2", "title 3"],
            "cow": ["title 1", "title 2", "title 3]
        }

    """
    word_list = get_word_list()
    return get_titles_json(word_list)


def get_titles_json(word_list):
    """
    Return the top 3 search titles for each of the provided terms.

    Args:
        word_list: a list of strings

    Returns:
        json of the form
        {
            "flower": ["title 1", "title 2", "title 3"],
            "cow": ["title 1", "title 2", "title 3]
        }

    """
    result = {}
    for word in word_list:
        titles = get_top_three_titles(word)
        result[word] = titles

    return json.dumps(result)


def get_top_three_titles(search_term):
    """
    Return a list of the top three titles on duckduckgo.

    Check the redis cache, return result from cache if it exists,
    else search duckduckgo and return top three titles.

    Args:
        search_term: the term to be searched on duckduckgo

    Returns:
        A list of the top three titles on duckduckgo.

    """
    titles = redis_client.lrange(search_term, 0, -1)
    if not titles:
        raw_response = get_raw_response(search_term)
        titles = parse_titles(raw_response)
        if titles:
            redis_client.lpush(search_term, *titles)

    return titles


def parse_titles(raw_response):
    """
    Parse the html response to return top three titles.

    Args:
        raw_response: the raw html response from duckduckgo

    Returns:
        A list of the top three titles from duckduckgo

    """
    titles = []
    doc = document_fromstring(raw_response)
    results_div = doc.get_element_by_id(RESULT_DIV_ID)
    for element in results_div.find_class(RESULT_CLASS):
        title = element.find_class(TITLE_CLASS)[0].text_content()
        titles.append(title)
        if len(titles) >= 3:
            break

    return titles


def get_raw_response(search_term):
    """
    Query DuckDuckGo and returns the raw html.

    Args:
        search_term: the term to be queried

    Returns:
        A string containing the raw html response.

    """
    qs_dict = {
        "q": search_term
    }
    return requests.get(SEARCH_URL, params=qs_dict).text
