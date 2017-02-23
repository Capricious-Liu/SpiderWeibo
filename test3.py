import requests
from bs4 import BeautifulSoup


response = requests.get('http://jecvay.com')

soup = BeautifulSoup(response.text)

print(soup.body.text)
# print(soup.find("input", {"name": "_xsrf"})['value'])
# print(soup.find("input", {"name": "_xsrf"})['value'])
# print(soup.title.text)

# print(soup.body.text)
# for x in soup.findAll("a"):
#     print(x['href'])