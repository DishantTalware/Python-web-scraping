import requests
from lxml import html

page = 1
while True:

    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    if response.status_code !=200:
        break
    tree = html.fromstring(response.content)

    quotes = tree.xpath('//span[@class="text"]/text()')
    author = tree.xpath('//small[@class="author"]/text()')
    tags = tree.xpath('//div[@class="tags"]')

    if not quotes:
        break

    for i in range(len(quotes)):
        tags_pipe = tags[i].xpath('.//a[@class="tag"]/text()')

        print("Description:", quotes[0] if quotes else "")
        print("Author:", author[0] if author else "")
        print("Tags:", ' | '.join(tags_pipe)),
        print("-" * 50)

    page += 1


#  ------------------------ mongodb connection  -------------------------------------------------------------
# ___________________________________________________________________________________________________________


# import requests
# from lxml import html
# from pymongo import MongoClient
#
# client = MongoClient('mongodb://localhost:27017/')
# db = client['3_pagination']
# collection = db['quotes']
#
# page = 1
# while True:
#     url = f'https://quotes.toscrape.com/page/{page}/'
#     response = requests.get(url)
#
#     if response.status_code != 200:
#         break
#     tree = html.fromstring(response.content)
#
#     quotes = tree.xpath('//span[@class="text"]/text()')
#     authors = tree.xpath('//small[@class="author"]/text()')
#     tags = tree.xpath('//div[@class="tags"]')
#
#     if not quotes:
#         break
#
#     # all_quotes = []
#     for i in range(len(quotes)):
#         tags_pipe = tags[i].xpath('.//a[@class="tag"]/text()')
#
#         data = {
#             'description :' : quotes[0],
#             'author :' : authors[0],
#             'tags :' : ' | '.join(tags_pipe),
#         }
#         collection.insert_one(data)
#
#     page += 1
