#!/usr/bin/python3
'''
Contains a script that starts a flask application
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Returns a string'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Returns a string'''
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
