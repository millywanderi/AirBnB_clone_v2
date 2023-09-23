#!/usr/bin/python3
"""Starts flask app listening to 0.0.0.0: port:5000
Route is /cities_by_states: and display HTML page with a list of all states
and related cities
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all State objects in DBStorage
    States/Cities are sorted by name.
    """
    states = storage.all(State)
    path = '8-cities_by_states.html'
    return render_template(path, states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
