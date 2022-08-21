# Import required web scraping libraries
import requests
import lxml
import bs4

# Goal is to grab all the quotes from https://quotes.toscrape.com

# Set variables you want to be consistent regardless of loop iteration
page_num = 1
quotes = []
scrape = True

# Use a while loop because it allows you run all the 
while scrape == True:
    try:
#         '''
#         Grab the url.
#         URL is conditionally formatted so that you can grab each page number
#         '''
        page_url = f"https://quotes.toscrape.com/page/{page_num}/"
        request = requests.get(page_url)
        
#         '''
#         Convert the request.text into a beautiful soup item using the BeautifulSoup() method
#         '''
        soup = bs4.BeautifulSoup(request.text, "lxml")

#         ''' 
#         Check if you've reached the end of the page. 
#         Once you finish scraping all the pages with quotes,
#         soup.select(".text") will give you [].
#         End the loop once this happens
#         '''
        if soup.select(".text") == []:
            print(f"No more quotes found on page {page_num}")
            scrape = False
            break
        
#         '''
#         Grab each quote and store the text in an outer variable quotes
#         '''
        quotes_html = soup.select(".text")
        for quote in quotes_html:
            quotes.append(quote.getText())
        
#         '''
#         Print summary of webscraping page
#         '''
        print(page_url)
        print(f"Found {len(quotes_html)} quotes on page {page_num} of website")
        
#         '''
#         Increase counter to increment to next page
#         '''
        page_num += 1
        
#     '''
#     Also end the loop if an HTTP request is returns an error
#     '''        
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error code: {err.response.status_code}")
        scrape = False

        
# '''
# Print your final outputs
# '''
print("="*100)
print("pages done scraping")
print("="*100)
nl = "\n"
print(f"All the quotes on the website are: \n{nl.join(quotes)}")