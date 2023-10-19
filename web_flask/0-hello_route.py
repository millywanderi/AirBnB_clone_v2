#!/usr/bin/python3
"""
Script that starts a Flask web application
Listens to 0.0.0.0, port 5000
Route '/airbnb-onepage/' displays Hello HBNB!
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
