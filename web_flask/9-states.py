#!/usr/bin/python3
"""
script that starts a Flask web application, fetch data from the storage engine
and load all cities of a State using route '/states/<id>'
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays a HTML page with a list of all states"""
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route('/states/<id>')
def states_list(id):
    """Render template with states"""
    for state in storage.all(State).value():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def app_teardown(exc):
    """Clean-up session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
