# ------------------------ All Posts [100 posts] -------------------------------------
import requests
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
data = response.json()

for item in data:
    print("userId :",item['userId'])
    print("Id :", item['id'])
    print("title :", item['title'])
    print("body :", item['body'])
    print('-'*50)



# ------------------------ All comments [500 comments] -------------------------------------
import requests
url = 'https://jsonplaceholder.typicode.com/comments'
response = requests.get(url)
data = response.json()

for item in data:
    print("postId :", item['postId'])
    print("id :",item['id'])
    print("name :", item['name'])
    print("email :", item['email'])
    print("body :", item['body'])
    print('-'*50)



# ------------------------ All albums [100 albums] -------------------------------------
import requests
url = 'https://jsonplaceholder.typicode.com/albums'
response = requests.get(url)
data = response.json()

for item in data:
    print("userId :", item['userId'])
    print("id :",item['id'])
    print("title :", item['title'])
    print('-'*50)



# ------------------------ All photos [5000 photos] -------------------------------------
import requests
url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
data = response.json()

for item in data:
    print("albumId :", item['albumId'])
    print("id :",item['id'])
    print("title :", item['title'])
    print("url :", item['url'])
    print("thumbnailUrl :", item['thumbnailUrl'])
    print('-'*50)




# ------------------------ All todos [100 todos] -------------------------------------
import requests
url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)
data = response.json()

for item in data:
    print("userId :", item['userId'])
    print("id :",item['id'])
    print("title :", item['title'])
    print("completed :", item['completed'])
    print('-'*50)




# ------------------------ All users [100 users] -------------------------------------
import requests
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
data = response.json()

for item in data:
    print("id :",item['id'])
    print("name :",item['name'])
    print("username :",item['username'])
    print("email :",item['email'])
    print("address :",item['address'])
    print("geo",item['address']['geo'])
    print("phone :",item['phone'])
    print("website",item['website'])
    print("company",item['company'])
    print('-'*150)
