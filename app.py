from flask import Flask
from source.histogram import histogram, sample

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello_world():
    dictionary = histogram('source/histogram - 10000 tests.txt')
    return dictionary