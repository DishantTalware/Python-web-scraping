# ______________________ Fetch All Categories ________________________________________________
# ____________________________________________________________________________________________

import requests
from lxml import html
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['4_only_categories']
collection = db['categories']

url = "https://quotes.toscrape.com/"
response = requests.get(url)
tree = html.fromstring(response.content)

category = tree.xpath('//span[@class="tag-item"]//a[@class="tag"]/text()')
# print(category)

# all_data = []
for categories in category:
    data = {
        'all_categories': categories,
    }
    collection.insert_one(data)

#     all_data.append(data)
# if all_data:
#     collection.insert_many(all_data)
# else:
#     print("No data found")




# ______________________ Fetch Categories with all data ______________________________________
# __________________  only 1 page scrape _____________________________________________________

# import requests
# from lxml import html
# from pymongo import MongoClient
#
# client = MongoClient("mongodb://localhost:27017/")
# db = client['4_all_categories']
# collection = db['all_categories']
#
# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# tree = html.fromstring(response.content)
#
# category = tree.xpath('//span[@class="tag-item"]//a[@class="tag"]/text()')
#
# for categories in category:
#     category_url = f"{url}/tag/{categories}/"
#     cat_url = requests.get(category_url)
#     cat_tree = html.fromstring(cat_url.content)
#
#     quote_boxes = cat_tree.xpath('//div[@class="quote"]')
#
#     for box in quote_boxes:
#         description = box.xpath('.//span[@class="text"]/text()')[0]
#         author = box.xpath('.//small[@class="author"]/text()')[0]
#         tags = box.xpath('.//div[@class="tags"]/a/text()')
#
#         # print("Category:", category)
#         # print("Description:", description)
#         # print("Author:", author)
#         # print("Tags:", tags)
#         # print("-" * 40)
#
#         data = {
#             'Category': categories,
#             'Description': description,
#             'Author': author,
#             'Tags': tags,
#         }
#         collection.insert_one(data)




# ______________________ Fetch Categories with all data ______________________________________
# __________________ all pages scrape _____________________________________________________

# import requests
# from lxml import html
# from pymongo import MongoClient
#
# client = MongoClient("mongodb://localhost:27017/")
# db = client['4_all_categories']
# collection = db['all_categories']
#
# BASE_URL = "https://quotes.toscrape.com"
#
# response = requests.get(BASE_URL)
# tree = html.fromstring(response.content)
#
# categories = tree.xpath('//span[@class="tag-item"]//a[@class="tag"]/text()')
#
# for category in categories:
#     print(f"\nScraping category: {category}")
#
#     page = 1
#     while True:
#         if page == 1:
#             category_url = f"{BASE_URL}/tag/{category}/"
#         else:
#             category_url = f"{BASE_URL}/tag/{category}/page/{page}/"
#
#         res = requests.get(category_url)
#         cat_tree = html.fromstring(res.content)
#
#         quote_boxes = cat_tree.xpath('//div[@class="quote"]')
#
#         if not quote_boxes:
#             break
#
#         for box in quote_boxes:
#             description = box.xpath('.//span[@class="text"]/text()')[0]
#             author = box.xpath('.//small[@class="author"]/text()')[0]
#             tags = box.xpath('.//div[@class="tags"]/a/text()')
#
#             data = {
#                 "category": category,
#                 "description": description,
#                 "author": author,
#                 "tags": ' | '.join(tags),
#             }
#
#             collection.insert_one(data)
#             print("Inserted:", description[:40], "...")
#
#         next_page = cat_tree.xpath('//li[@class="next"]/a')
#
#         if next_page:
#             page += 1
#         else:
#             break














