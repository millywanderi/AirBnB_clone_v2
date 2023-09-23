#!/usr/bin/python3
"""Starts flask app listening to 0.0.0.0: port:5000"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Displays an HTML page with a list of all State objects in DBStorage
    States are sorted by name.
    """
    path = '7-states_list.html'
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
