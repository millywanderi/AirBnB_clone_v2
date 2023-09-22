#!/usr/bin/python3
"""
Script that starts a Flask web application
Listens to 0.0.0.0, port 5000
Route '/' displays “C ” followed by the value of the text variable
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """returns c followed by text"""
    text = escape(text).replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is cool'):
    """returns python is cool"""
    text = text.replace('_', ' ')
    return "Python %s" % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
