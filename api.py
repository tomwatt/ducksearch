"""A web service for retrieving search result titles from duckduckgo."""
from flask import Flask
from ducksearch import get_top_three_titles_json

app = Flask(__name__)

@app.route('/search/duckduckgo/<search_term>')
def duck_search(search_term):
    """
    Return a json array of the top three titles from duckduckgo.

    Args:
        search_term: the term to be searched on duckduckgo

    Returns:
        A json array containing the top three titles from duckduckgo.

    """
    return get_top_three_titles_json(search_term)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
