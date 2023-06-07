import bs4
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones/touch')
soup = BeautifulSoup(url.text, 'html.parser')

product_name = soup.find_all('a', class_ = 'title')


prices = soup.find_all('h4', class_ ='pull-right price')

reviews = soup.find_all('p', class_ = 'pull-right')

descriptions = soup.find_all('p', class_ ='description')

product_name_list = []
for product in product_name:
    if isinstance(product, bs4.element.Tag) and hasattr(product, 'string') and product.string is not None:
        title_product = product.string
        # print(title_product)
        product_name_list.append(title_product)

prices_list = []
for price in prices:
    if isinstance(price, bs4.element.Tag) and hasattr(price, 'string') and price.string is not None:
        title_price = price.string
        # print(title_price)
        prices_list.append(title_price)

reviews_list = []
for review in reviews:
    if isinstance(review, bs4.element.Tag) and hasattr(review, 'string') and review.string is not None:
        title_review = review.string
        reviews_list.append(title_review)

descriptions_list = []
for description in descriptions:
    if isinstance(description, bs4.element.Tag) and hasattr(description, 'string') and description.string is not None:
        title_description = description.string
        descriptions_list.append(title_description)

table = pd.DataFrame({'Product Name':product_name_list, 'Description': descriptions_list,'Price': prices_list,'Review': reviews_list })
print(table)