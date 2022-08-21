# web_scraping_projects_and_tips
This repository will be used to showcase (most of) my web scraping projects

# Important functions for webscraping

## Import required libraries
- The required libraries for webscraping are:

```python
import requests
import lxml
import bs4
```

- `requests` is used to make HTTP requests and extract HTML code from a URL
- `lxml` is used to process XML and HTML code in python
- `bs4` aka `BeautifulSoup Version 4` is used for pulling data out of HTML and XML files. 

## Make an HTTP request
- Making an HTTP request is done by using the `.get()` method of `requests`
- e.g.

```python
request = requests.get("https://www.example.com/")
```

- The HTML of the website is then stored inside the `.text` attribute of the request instance (in string form)
  - The request instance is of class `requests.models.Response`
  
```python
request.text
'''
OUTPUTS
'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'
'''

type(request.text)
'''
OUTPUTS
<class 'str'>
'''

type(request)
'''
OUTPUTS
<class 'requests.models.Response'>
'''
```
