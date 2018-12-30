from flask import Flask, jsonify, request
from Summarizer import summarizer


app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 8081


@app.route('/', methods=['POST'])
def summary():
    data = request.get_json(force=True)
    data_pred = data['data']

    pred_text = summarizer(data_pred)
    output = {'prediction': pred_text}

    return jsonify(output)


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
