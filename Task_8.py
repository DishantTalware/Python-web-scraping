import requests
from lxml import html
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['7_book_to_scrape']
categories = db['book_to-scrape']

page = 1
while True:

    url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url)

    if response.status_code != 200:
        break
    tree = html.fromstring(response.content)
    books = tree.xpath('//article[@class="product_pod"]')

    for book in books:
        title = book.xpath('.//h3/a/@title')[0]
        classes = book.xpath('.//p[contains(@class,"star-rating")]/@class')[0]
        rating = classes.replace('star-rating', '').strip()
        price = book.xpath('.//p[@class="price_color"]/text()')[0]
        availability = "".join(book.xpath('.//p[contains(@class,"availability")]//text()')).strip()

        scraped = {
            'Title': title,
            'Rating': rating,
            'Price': price,
            'Availability': availability,
        }
        categories.insert_one(scraped)

    page += 1
