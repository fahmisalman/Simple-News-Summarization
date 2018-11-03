from flask import Flask, abort, jsonify, request, current_app
from Web_scraper import *
import json
import Summarizer as summarize


app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 8081

with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)


@app.route('/', methods=['POST'])
def summary():
    # use parser and find the user's query
    data = request.get_json(force=True)
    data_pred = data['data']

    pred_text = summarize.summarizer(data_pred)
    output = {'prediction': pred_text}

    return jsonify(output)


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)

    # url = 'http://0.0.0.0:8081/'
    # data = json.dumps({'data': get_article('https://news.detik.com/internasional/d-4281502/pakistan-bebaskan-wanita-yang-divonis-mati-atas-penistaan-agama')})
    # # r = request.post(url, data)
    # print(json.loads(data)['data'])
    # # print(r.json)
