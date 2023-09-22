#!/usr/bin/python3
"""
Script that starts a Flask web application
Listens to 0.0.0.0, port 5000
Route '/number_odd_or_even/<n>' displays html if n is an int
"""
from flask import Flask, escape, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns n if the number is an int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """returns HTML page only if n is an int"""
    return render_template("5-number.html", n=n)


@app.roue('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """displays html if n is an int"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
