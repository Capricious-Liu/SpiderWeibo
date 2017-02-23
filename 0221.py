import requests
from bs4 import BeautifulSoup

param = {'wd': '123'}

r = requests.get('http://baidu.com/s', params=param)

# print(r.url)
r = requests.get('https://baidu.com/s?wd=123')

soup = BeautifulSoup(r.text)

print(soup.body.text)
