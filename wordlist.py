"""A module for retrieving a list of words."""
import random
import requests

WORD_LIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
NUMBER_OF_WORDS = 100


def get_word_list(list_size=NUMBER_OF_WORDS):
    """
    Retrieve a list of words.

    Pulls list from from an online repo, filters it, then returns
    a number (default = 100) of randomly selected words.

    Filter: only allow words that begin with a lowercase letter, and only
    contain letters.

    Args:
        list_size (optional): the number of words to be returned, default = 100.

    Returns:
        A list of strings

    """
    raw_response = requests.get(WORD_LIST_URL).text
    raw_list = parse_raw_response(raw_response)
    return filter_list(raw_list, list_size)


def filter_list(word_list, list_size):
    """
    Filter the provided list, and return the first list_size entries.

    Args:
        word_list: unfiltered list of strings
        list_size: the number of results to be returned

    Returns:
        A list of strings, size = list_size

    """
    result = set()
    while len(result) <= list_size:
        word = random.choice(word_list)
        if word[0].islower() and word.isalpha() and word not in result:
            result.add(word)

    return list(result)



def parse_raw_response(raw_response):
    r"""
    Parse raw response and return list of strings.

    Args:
        raw_response: A string in the format "lots\nof\nwords"

    Returns:
        A list of strings

    """
    return raw_response.split("\n")
