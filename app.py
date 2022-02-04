from flask import Flask
from histogram import histogram, sample

app = Flask(__name__)

@app.route("/")
def hello_world():
    dictionary = histogram('histogram - 10000 tests.txt')
    return dictionary