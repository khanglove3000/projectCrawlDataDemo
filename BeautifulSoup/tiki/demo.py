import requests
from bs4 import BeautifulSoup
req = requests.get('https://shopee.vn/M%C3%A1y-T%C3%ADnh-Laptop-cat.11035954')
print(req.text)