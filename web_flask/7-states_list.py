#!/usr/bin/python3
'''
Contains a script that starts a flask application
'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Returns a template with all the states in storage'''
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    '''Removes current session after each request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

