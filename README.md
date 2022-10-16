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
>>> request = requests.get("https://www.example.com/")
```

- The HTML of the website is then stored inside the `.text` attribute of the request instance (in string form)
  - The request instance is of class `requests.models.Response`
  
```python
>>> request.text
'''OUTPUTS
'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'
'''

>>> type(request.text)
'''OUTPUTS
<class 'str'>
'''

>>> type(request)
'''OUTPUTS
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
>>> soup = bs4.BeautifulSoup(request.text, "lxml")

>>> soup
'''OUTPUTS
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
>>> type(soup)
'''OUTPUTS
<class 'bs4.BeautifulSoup'>
'''
```

## Grabbing elements and classes with BeautifulSoup

- Grabbing HTML elements can be done using the `.select()` method of BeautifulSoup

 - To grab tags, simply use `soup.select("tag")`
   - e.g. `soup.select("div")` grabs all element with the &lt;div> tag 
 - To grab classes, use `soup.select(".some_class")`
 - To grab ids, use `soup.select("#some_id")`
  - To grab elements within elements, use `soup.select("tag1 tag2")`
   - e.g. `soup.select("div span")` grabs all &lt;span> elements that are within &lt;div> tags
  - To grab elements directly within elements, use `soup.select("tag1 > tag2")`
    - e.g. `soup.select("div > span")` grabs all &lt;span> elements that are directly within &lt;div> tags, with nothing in between

      - This nomenclature is very similar to CSS selectors

- e.g. grabbing paragraph elements from www.example.com

```python
>>> soup.select("p")
'''OUTPUTS
[<p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>, <p><a href="https://www.iana.org/domains/example">More information...</a></p>]
'''
```
  
- You can also select elements within elements with another `.select` call

```python
>>> soup.select("p")[1]
'''OUTPUTS
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
'''

>>> soup.select("p")[1].select("a")
'''OUTPUTS
[<a href="https://www.iana.org/domains/example">More information...</a>]
'''
```

- The type of this element is also not a string, but rather a `bs4.element.Tag` so you can do some more scraping and data extracting from it using BeautifulSoup methods

```python
>>> type(soup.select("p")[1].select("a")[0])
'''OUTPUTS
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
<p> This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
'''

>>> soup.select("p")[0].getText()
'''OUTPUTS
'This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.'
'''
```

# Scraping videos
 - Organize notes about `youtube-dl`, `gallery-dl` (for twitter), `--postprocessor-args "-ss x:xx:xx.xx -t xx:xx:xx.xx"`, grabbing things from the network tab of chrome-dev tools, `nohup ... &` and the difference between `youtube-dl` and `ffmpeg`.
 - Some forum posts that helped you before
    - https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command
 - Helpful website to work with `postprocessor-args`
    - https://www.calculator.net/time-calculator.html?tcday1=&tchour1=4&tcminute1=53&tcsecond1=55&Op=-&tcday2=&tchour2=4&tcminute2=22&tcsecond2=7&tcday3=&tchour3=&tcminute3=&tcsecond3=&ctype=1&x=98&y=12
    - i.e. 
      - Enter the end timestamp of the video you want to scrape
      - Subtract the initial timestamp of the video you want 
      - Outputs minutes in decimals (e.g. 31.8 minutes). Grab decimal and multiply by 60 to get seconds (e.g. 60 * 0.8 = 48s; total time = 31min48s)
      - input time for your `-t` argument
 - Some commands to remind you of what you've done before
 ```
ffmpeg -ss 5:59:17 -i "https://184vod-adaptive.akamaized.net/exp\=1664533949\~acl\=%2F282eb4d9-350e-40cf-9e05-37b0e2149a8f%2F%2A\~hmac\=d08b342e69f532034932d3479a0c097043d26a94934d11dfcf6126b210caccb9/282eb4d9-350e-40cf-9e05-37b0e2149a8f/sep/video/1222279f,de1af7de,b93f4bfc,42a59416,ff3118a4/audio/7ad16d49,841db898/master.mpd\?query_string_ranges\=1\&base64_init\=1" -ss 5:59:17 -i "https://184vod-adaptive.akamaized.net/exp\=1664533949\~acl\=%2F282eb4d9-350e-40cf-9e05-37b0e2149a8f%2F%2A\~hmac\=d08b342e69f532034932d3479a0c097043d26a94934d11dfcf6126b210caccb9/282eb4d9-350e-40cf-9e05-37b0e2149a8f/sep/video/1222279f,de1af7de,b93f4bfc,42a59416,ff3118a4/audio/7ad16d49,841db898/master.mpd\?query_string_ranges\=1\&base64_init\=1" -t 7:05 -map 0:v -map 1:a -c:v libx264 -c:a aac ~/Dropbox/UWO/grad_school/ben_scott_foundry_presentation.mkv\n

nohup youtube-dl https://vimeo.com/715755275 --video-password 5YN8IO-2022  --postprocessor-args "-ss 5:59:17.00 -t 00:07:05.00" -o ~/Dropbox/UWO/grad_school/ben_scott_foundry_presentation.mp4 &

gallery-dl https://twitter.com/Iamthetimby/status/1555702108833423364 -o "test"

nohup youtube-dl -o chamber_media_ad_research https://www.facebook.com/RussellBrunsonLIVE/videos/511628290475707 --add-header "cookie: datr=LphrYBGMEwqPLovPkyV7h_nd; sb=iqBrYGIo3o-VCNH_zlq6Jts5; c_user=100013504470708; m_page_voice=100013504470708; m_pixel_ratio=2; dpr=2; xs=16%3AgClNpzs0H_sjyw%3A2%3A1637379051%3A-1%3A14923%3A%3AAcXb6-81kmqLdYQYVvHpWPuXZf1HJY_w2XI9pJyDIz-Y; fr=0ODlb7aGYdu2HameH.AWX-gM3DpK5h_TfIkbNjMPOWRaQ.BjS1xZ.Cg.AAA.0.0.BjS1xZ.AWV6NCe6rgY; presence=C%7B%22t3%22%3A%5B%7B%22i%22%3A%22u.100010631477740%22%7D%2C%7B%22i%22%3A%22g.5664680843541958%22%7D%2C%7B%22i%22%3A%22g.5482284065183654%22%7D%5D%2C%22utc3%22%3A1665883241375%2C%22v%22%3A1%7D; wd=1440x393" --postprocessor-args "-ss 4:22:52.00 -t 00:31:48.00" &
 ```
