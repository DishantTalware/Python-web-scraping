# -------------------------    only first page ka data fetch   ---------------------------------------
# ____________________________________________________________________________________________________
import requests
from lxml import html

url = "https://quotes.toscrape.com/"
response = requests.get(url)
tree = html.fromstring(response.content)

quote_boxes = tree.xpath('//div[@class="quote"]')


for box in quote_boxes:
    description = box.xpath('.//span[@class="text"]/text()')
    author = box.xpath('.//small[@class="author"]/text()')
    tags = box.xpath('.//div[@class="tags"]/a[@class="tag"]/text()')
    tag_pipeline = " | ".join(tags)

    print("Description:", description[0] if description else "")
    print("Author:", author[0] if author else "")
    print("Tags:", tag_pipeline)
    print("-" * 50)









#-----------------------------  mongodb connection ------------------------------------------------------------
# --------------- insert_one ------------------------------------------------------------------------------
# fkt 2 kam kele mongo connection and last mdhe data insert kela ahe

''' only use
        client = MongoClient("mongodb://localhost:27017/")
        db = client['one_page_fetching']
        collection = db['quotes']

        and

        collection.insert_one(data)'''

# import requests
# from lxml import html
# from pymongo import MongoClient
#
# client = MongoClient("mongodb://localhost:27017/")
# db = client['2_one_page_fetching']
# collection = db['quotes']
#
# url = "https://quotes.toscrape.com/"
# response = requests.get(url)
# tree = html.fromstring(response.content)
#
# quote_boxes = tree.xpath('//div[@class="quote"]')
#
# for box in quote_boxes:
#     quote = box.xpath('.//span[@class="text"]/text()')
#     author = box.xpath('.//small[@class="author"]/text()')
#     tags = box.xpath('.//div[@class="tags"]//a[@class="tag"]/text()')
#     tag_pipeline = ' | '.join(tags)
#
#     data ={
#         'description': quote[0],
#         'author': author[0],
#         'tags': tag_pipeline
#     }
#
#     collection.insert_one(data)








#-----------------------------  mongodb connection ------------------------------------------------------------
# --------------- insert_many ------------------------------------------------------------------------------

# import requests
# from lxml import html
# from pymongo import MongoClient
#
#
# client = MongoClient("mongodb://localhost:27017/")
# db = client['2_one_page_fetching']
# collection = db['quotes']
#
# url = "https://quotes.toscrape.com/"
# response = requests.get(url)
# tree = html.fromstring(response.content)
#
# quote_boxes = tree.xpath('//div[@class="quote"]')
#
# all_quote = []
# for box in quote_boxes:
#     quote = box.xpath('.//span[@class="text"]/text()')
#     author = box.xpath('.//small[@class="author"]/text()')
#     tags = box.xpath('.//div[@class="tags"]//a[@class="tag"]/text()')
#     tag_pipeline = ' | '.join(tags)
#
#     data ={
#         'description': quote[0],
#         'author': author[0],
#         'tags': tag_pipeline
#     }
#     all_quote.append(data)
#
# if all_quote:
#     collection.insert_many(all_quote)
# else:
#     print("No quotes found")