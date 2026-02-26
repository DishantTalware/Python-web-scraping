import requests
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['11_json_data_sepratefile']
collection = db['json']

endpoints = ['posts', 'comments', 'albums', 'photos', 'todos', 'users']

for endpoint in endpoints:
    url = f"https://jsonplaceholder.typicode.com/{endpoint}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data")
        continue
    data = response.json()

    collection = db[endpoint]
    collection.delete_many({})
    collection.insert_many(data)

    print(f"Inserted {len(data)} records for '{endpoint}'")
