#!/usr/bin/python3
""" A script that starts a flask web app listening on 0.0.0.0, port 5000
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display C followed by value of text variable
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# New dynamic route
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Replace underscores with spaces in the text"""
    display_text = text.replace('_', ' ')
    return 'C {}'.format(display_text)


if __name__ == "__main__":
    # çonfigure the app to listen on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
