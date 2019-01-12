from flask import Flask, jsonify, request, flash, redirect
from Model import App


app = Flask(__name__)


def upload_file(req):
    """
    Upload file to server
    :param req: Request file
    :return: File path
    """
    link = req.files['image']
    if link.filename == '':
        flash('No selected file')
        return redirect(req.url)
    else:
        return link.filename


@app.route('/', methods=['POST'])
def summary():
    result = ''
    if request.method == 'POST':
        link = request.form['url']
        result = App.fit(link)
    return jsonify(result)


def main(host='0.0.0.0', port=8081):
    app.run(host=host,
            debug=True,
            port=port)
