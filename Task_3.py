import  requests
from lxml import html

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
tree = html.fromstring(response.content)

quotes = tree.xpath('//div[@class="quote"]')

with open("quotes.txt", "w", encoding="utf-8") as file:
    for box in quotes:
        description = box.xpath('.//span[@class="text"]/text()')
        author = box.xpath('.//small[@class="author"]/text()')
        tags = box.xpath('.//div[@class="tags"]/a[@class="tag"]/text()')
        tag_pipeline = " | ".join(tags)

        # WRITE INTO FILE
        file.write(f'Description : {description}\n')
        file.write(f'Author : {author}\n')
        file.write(f'Tags : {tag_pipeline}\n')
        file.write("-" * 50 + "\n")

        # print on terminal
        print("Description:", description[0] if description else "")
        print("Author:", author[0] if author else "")
        print("Tags:", tag_pipeline)
        print("-" * 50)

