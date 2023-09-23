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
@app.route('/states/<id>')
def states_list(id=None):
    """Render template with states"""
    path = '9-states.html'
    states = storage.all(State)
    return render_template(path, states=states, id=id)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
