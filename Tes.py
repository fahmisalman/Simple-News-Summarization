import requests
from Web_scraper import *
import json

# app_context = app.app_context()
# app_context.push()

# print(app.name)

url = 'http://0.0.0.0:8081/'
data = json.dumps({'data': get_article('https://news.detik.com/internasional/d-4281502/pakistan-bebaskan-wanita-yang-divonis-mati-atas-penistaan-agama')})
r = requests.post(url, data)
print(r.json())


# d1 = {"('Hello',)": 6, "('Hi',)": 5}
# s1 = json.dumps(d1)
# d2 = json.loads(s1)
#
# print(d1, s1, d2)