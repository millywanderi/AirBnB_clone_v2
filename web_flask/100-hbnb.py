#!/usr/bin/python3
"""Start a flask application"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """Displays HBNB filter page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
