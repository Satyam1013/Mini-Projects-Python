import requests;
import json

query = input('Search Topics: ')

url = f'https://newsapi.org/v2/top-headlines?q={query}&from=2023-04-06&sortBy=publishedAt&apiKey=f1d33e56a2fd487bb4d98977ed734479'

res = requests.get(url)
news = json.loads(res.text)

for news in news['articles']:
    print(news['title'])
    print(news['description'])
    print('-----------')

# print(res.text)