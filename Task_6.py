import requests
from lxml import html
from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")
db = client["categories_with_status"]
category_col = db["categories"]
quotes_col = db["quotes"]

url = "https://quotes.toscrape.com/"
response = requests.get(url)
tree = html.fromstring(response.content)

categories = tree.xpath('//span[@class="tag-item"]/a/text()')

for category in categories:
    category_url = f"https://quotes.toscrape.com/tag/{category}/"

    if not category_col.find_one({"category": category}):
        category_col.insert_one({
            "category": category,
            "category_url": category_url,
            "status": "pending"
        })

pending_categories = category_col.find({"status": "pending"})

for cat in pending_categories:
    response = requests.get(cat["category_url"])
    tree = html.fromstring(response.content)

    quotes = tree.xpath('//div[@class="quote"]')

    for q in quotes:
        description = q.xpath('.//span[@class="text"]/text()')
        author = q.xpath('.//small[@class="author"]/text()')
        tags = q.xpath('.//a[@class="tag"]/text()')

        quotes_col.insert_one({
            "category": cat["category"],
            "description": description[0] if description else "",
            "author": author[0] if author else "",
            "tags": tags
        })

    category_col.update_one(
        {"_id": cat["_id"]},
        {"$set": {"status": "done"}}
    )
    time.sleep(1)
print("All categories processed successfully")
