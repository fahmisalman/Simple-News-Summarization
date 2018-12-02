from Web_scraper import *
import requests
import json


url = 'http://0.0.0.0:8081/'
data = json.dumps({'data': get_article('https://news.detik.com/internasional/d-4281502/pakistan-bebaskan-wanita-yang-divonis-mati-atas-penistaan-agama')})
r = requests.post(url, data)
print(r.json())
