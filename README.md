# DuckDuckGo service

A proxy service for retrieving the top titles for search terms from DuckDuckGo


## Getting Started

From the root of the project, run the following command to start a working version of the  application:

docker-compose up --build

Navigate to http://127.0.0.1:5000/search/duckduckgo/{search term}, or wherever you have it hosted, to view the search results.

To see the results to assignment one, set the application running with the command above,
then open a terminal in the container with the following command:

docker-compose exec ducksearch sh

From here you can open up a python interpreter and play around. For the results to assignment one:

import ducksearch
ducksearch.search_word_list()


### Prerequisites

Make sure you have docker and docker compose installed.


## Testing

To run the full suite of unit tests, enter the following command from the root of the project:

python -m unittest

Testing output will be displayed in the terminal.


## Coding Style

The project uses pylint and pydocstyle for linting.



## Authors

* **Tom Watt** - [tom.watt@protonmail.com]
