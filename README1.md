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

## Convert HTML string into *soup* object
- The string notation of HTML isn't very useful for extracting data, so after the HTML code is pulled it needs to be made more python friendly using the BeautifulSoup package
  - Python friendly HTML will hereby be referred to as *soup* 
- Creating a soup is done by using the `.BeautifulSoup()` method of `bs4`
  - `.BeautifulSoup()` takes 2 arguments
    - The string notation of HTML (found in the `.text` attribute of the request instance 
    - An HTML parser (typically will always be `"lxml"`
      - This is why `import lxml` is necessary at the start of the script

```python
soup = bs4.BeautifulSoup(request.text, "lxml")

soup
'''
OUTPUTS
<!DOCTYPE html>
<html>
<head>
<title>Example Domain</title>
<meta charset="utf-8"/>
<meta content="text/html; charset=utf-8" http-equiv="Content-type"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
'''
```

- soup objects are not stored as strings, but rather as special BeautifulSoup instances

```python
type(soup)
'''
OUTPUTS
<class 'bs4.BeautifulSoup'>
'''
```

## Grabbing elements and classes with BeautifulSoup

- Grabbing HTML elements can be done using the `.select()` method of BeautifulSoup
  - To grab tags, simply use `soup.select("tag")`
    - e.g. `soup.select("div")` grabs all element with the <div> tag 
  - To grab classes, use `soup.select(".some_class")`
  - To grab ids, use `soup.select("#some_id")`
  - To grab elements within elements, use `soup.select("tag1 tag2")`
    - e.g. `soup.select("div span")` grabs all <span> elements that are within <div> tags
  - To grab elements directly within elements, use `soup.select("tag1 > tag2")`
    - e.g. `soup.select("div > span")` grabs all <span> elements that are directly within <div> tags, with nothing in between
      - This nomenclature is very similar to CSS selectors

- e.g. grabbing paragraph elements from www.example.com

```python
soup.select("p")
'''
OUTPUTS
[<p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>, <p><a href="https://www.iana.org/domains/example">More information...</a></p>]
'''
```
  
- You can also select elements within elements with another `.select` call

```python
soup.select("p")[1]
'''
OUTPUTS
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
'''

soup.select("p")[1].select("a")
'''
OUTPUTS
[<a href="https://www.iana.org/domains/example">More information...</a>]
'''
```

- The type of this element is also not a string, but rather a `bs4.element.Tag` so you can do some more scraping and data extracting from it using BeautifulSoup methods

```python
type(soup.select("p")[1].select("a")[0])
'''
OUTPUTS
<class 'bs4.element.Tag'>'''
```

## Extracting attributes
- If an HTML element has attributes, they can be can be extracted essentially by doing a dictionary search on a `bs4.element.Tag` object using the attribute name as a key
- e.g.

```python
>>> soup.select("p")[1].select("a")[0]
'''OUTPUTS
<a href="https://www.iana.org/domains/example">More information...</a>
'''

# notice dict["key"] notation
>>> soup.select("p")[1].select("a")[0]["href"]
'''OUTPUTS
'https://www.iana.org/domains/example'
'''
```
## Extracting text between the tags
- Extracting text between tags can be done by using the `.getText()` method of `bs4`
- e.g.
  
```python

```python
>>> soup.select("p")[0]
'''OUTPUTS
<p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
'''

>>> soup.select("p")[1].select("a")[0]["href"]
'''OUTPUTS
'This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.'
'''
```


