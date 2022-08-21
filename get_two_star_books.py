# Import required web scraping libraries
import requests
import lxml
import bs4

# Goal is to grab all the two star book titles from https://books.toscrape.com

# Set variables you want to be consistent regardless of loop iteration
page_num = 1
two_star_product_titles = []
scrape = True

# Use a while loop because it allows you run all the 
while scrape == True:
    try:
#         '''
#         Set variables you want to reset after every iteration
#         '''
        two_star_products = []
        added_titles_counter = 0
        
#         '''
#         Grab the url.
#         URL is conditionally formatted so that you can grab each page number
#         '''
        book_url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
        bookstore = requests.get(book_url)
        
#         '''
#         The raise_for_status() method will give an exception if an HTTP error is reached
#		  This line is what triggers the except block when the web scraping is finished
#         '''
        bookstore.raise_for_status()
        
#         '''
#         Convert the request.text into a beautiful soup item using the BeautifulSoup() method
#         '''
        soup = bs4.BeautifulSoup(bookstore.text, "lxml")
        
#         '''
#         Grab all the products (book entries) from this page.
#         The book entries with two stars will be filted from this list
#         '''
        products = soup.select(".product_pod")
        
#         '''
#         Check if the book has two stars 
#         Can do this using products[0].select(".star-rating.Two")
#         If it does, it'll produce a populated list
#         If it doesn't, it'll produce and empty list ( [] )
#         '''
        for product in products:
            if product.select(".star-rating.Two") != []:
                two_star_products.append(product)
                added_titles_counter += 1
                
#         '''
#         From the book entries that have two stars, extract the titles of the books
#         Can do this using products[book_num].select("a")[1]["title"]
#         '''
        for prods in two_star_products:
            two_star_product_titles.append(prods.select("a")[1]["title"])
            
#         '''
#         Print summary of webscraping page
#         '''        
        print(book_url)
        print(f"page {page_num} scraped")
        print(f"added {added_titles_counter} books with 2 stars")

#         '''
#         Increase counter to increment to next page
#         '''
        page_num += 1
        
#     '''
#     If a page doesn't exist a 404 error will be outputted.
#     So end the loop if an HTTP request returns an error
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
print(f"The total number of books with 2 stars found is {str(len(two_star_product_titles))}")
nl = "\n"
print(f"The title of the books is with 2 stars are \n{'='*100}\n-{(nl+'-').join(two_star_product_titles)}")