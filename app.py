from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/query', methods=['POST', 'GET'])
def query():
    from data.graphOL import download_all_file
    download_all_file()
    return render_template("index.html")


@app.route("/")
def index():
    return render_template("index.html")



