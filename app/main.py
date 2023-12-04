"""
This is the main file of the Flask application.
"""

from typing import Any
import os
from flask import Flask, render_template
# from flask import request
# from . import forms
from . import db_api

app = Flask(__name__)
app.secret_key = 'b720367a8089e1e1b15ba89252ce07'
app.secret_key += 'b8393320dad043d609c01366a6cfe7946e'


@app.route('/')
def home() -> Any:
    """Home page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    context = {
        'title': 'Sports Score Hub',
        'content': 'Your gateway to global sports results'
    }
    return render_template('home.html', **context)


@app.route('/baseball')
def baseball() -> Any:
    """Recipes page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    documents = db_api.find_all({})

    context = {
        'title': 'Baseball',
        'recipes': documents['documents']
    }
    return render_template('baseball.html', **context)


@app.route('/soccer')
def soccer() -> Any:
    """Recipes page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    documents = db_api.find_all({})

    context = {
        'title': 'Soccer',
        'recipes': documents['documents']
    }
    return render_template('soccer.html', **context)


@app.route('/mma')
def mma() -> Any:
    """Recipes page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    documents = db_api.find_all({})

    context = {
        'title': 'MMA',
        'recipes': documents['documents']
    }
    return render_template('mma.html', **context)


@app.route('/basketball')
def basketball() -> Any:
    """Recipes page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    documents = db_api.find_all({})

    context = {
        'title': 'Basketball',
        'recipes': documents['documents']
    }
    return render_template('basketball.html', **context)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5555))
    app.run(debug=True, host='0.0.0.0', port=port)
