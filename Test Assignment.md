# Notes
Both assignments must be done in Python 3 with the use of any packages you see fit. When assessing the results, we'll pay special attention to performance of your code, so try to make it optimized.

# Test Assignment No. 1
1. Get [a list](https://raw.githubusercontent.com/dwyl/english-words/master/words.txt) of English words.
2. Select 100 random entries that satisfy these conditions:
   * They begin with a lowercase letter.
   * They only contain letters.
3. Search those entries on [DuckDuckGo](https://duckduckgo.com).
4. Save the titles of top three results.

**Expected outcome**: a JSON of the following structure:
```
{"flower": ["title 1", "title 2", "title 3"], "cow": ["title 1", "title 2", "title 3], ...}
```

# Test Assignment No. 2
Turn the script you created earlier into a proxy service. It should response to `GET` requests at `/search/duckduckgo/{search term}` and return JSON arrays of up to three titles of the top results. Queries must be cached, so if a term is looked up twice, first it will be a request to DuckDuckGo and second will be a result from the cache. Write unit tests for your code with the use of `unittest` and `unittest.mock` modules.

**Expected outcome**: a publicly availble web service.
