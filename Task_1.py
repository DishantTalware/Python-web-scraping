import requests
from lxml import html

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
}

response = requests.get('https://quotes.toscrape.com/', headers=headers)
tree = html.fromstring(response.content)
quotes = tree.xpath('//div[@class="quote"]')

for quote in quotes:
    description = quote.xpath('.//span[@class="text"]/text()')
    author = quote.xpath('.//small[@class="author"]/text()')
    tags = quote.xpath('.//a[@class="tag"]/text()')

    data = {
        'description': description[0] if description else None,
        'author': author[0] if author else None,
        'tags': tags,
    }

    print(data)