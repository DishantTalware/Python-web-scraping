import requests
from lxml import html
from pymongo import MongoClient
from urllib.parse import urljoin

client = MongoClient("mongodb://localhost:27017/")
db = client["8_book_to_categories_wise"]
collection = db["books"]

BASE_URL = "https://books.toscrape.com/"

home = requests.get(BASE_URL)
tree = html.fromstring(home.content)

category_links = tree.xpath('//ul[@class="nav nav-list"]//a/@href')
category_names = tree.xpath('//ul[@class="nav nav-list"]//a/text()')
categories = list(zip(category_names, category_links))

categories = categories[1:]
for cat_name, cat_link in categories:
    cat_name = cat_name.strip()
    page = 1

    while True:
        page_url = urljoin(BASE_URL, cat_link.replace("index.html", f"page-{page}.html"))
        response = requests.get(page_url)

        if response.status_code != 200:
            break

        tree = html.fromstring(response.content)
        books = tree.xpath('//article[@class="product_pod"]')

        if not books:
            break

        for book in books:
            title = book.xpath('.//h3/a/@title')[0]

            classes = book.xpath('.//p[contains(@class,"star-rating")]/@class')[0]
            rating = classes.replace("star-rating", "").strip()
            price = book.xpath('.//p[@class="price_color"]/text()')[0]
            availability = "".join(
                book.xpath('.//p[contains(@class,"availability")]//text()')
            ).strip()

            data = {
                "Category": cat_name,
                "Title": title,
                "Rating": rating,
                "Price": price,
                "Availability": availability
            }

            collection.insert_one(data)

        page += 1
