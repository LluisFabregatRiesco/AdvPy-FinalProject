"""
This is the main file of the Flask application.
"""

from typing import Any
import os
from flask import Flask, render_template
import db_api
import http.client
import json



app = Flask(__name__)


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


@app.route('/soccer')
def soccer() -> Any:
    """Soccer page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    context = {
        'title': 'Soccer',
    }
    return render_template('soccer.html', **context)


@app.route('/mma')
def mma() -> Any:
    """MMA page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    context = {
        'title': 'MMA',
    }
    return render_template('mma.html', **context)


@app.route('/basketball')
def basketball() -> Any:
    """Basketball page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    context = {
        'title': 'Basketball',
    }
    return render_template('Basketball.html', **context)


@app.route('/baseball')
def baseball() -> Any:

    """
    conn = http.client.HTTPSConnection("v1.baseball.api-sports.io")
    payload = ''
    headers = {
        'x-rapidapi-key': 'abcbccc15405752f45c03e02088526ca',
        'x-rapidapi-host': 'v1.baseball.api-sports.io'
    }

    for i in range(11, 20):
        conn.request("GET", "/teams?id="+str(i), payload, headers)
        res = conn.getresponse()
        data = res.read()
        j = data.decode("utf-8").replace("'", '"')

        dat = json.loads(j)
        print(dat["response"][0]["name"])

        db_api.insert_one({"Name": dat["response"][0]["name"],
        "ID": dat["response"][0]["id"]})

    """

    res = db_api.find_all({})

    

    context = {
        "title": "Baseball",
        "content": res["documents"]
    }

    return render_template('baseball.html', **context)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5555))
    app.run(debug=True, host='0.0.0.0', port=port)
