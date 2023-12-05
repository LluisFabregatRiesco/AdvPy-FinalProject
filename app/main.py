"""
This is the main file of the Flask application.
"""

from typing import Any
import os
import http.client
from flask import Flask, render_template
# from flask import request
# from . import forms
from . import db_api
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
    res = db_api.find_all({}, "baseball")
    context = {
        "title": "Baseball",
        "content": res["documents"]
    }
    return render_template('baseball.html', **context)


@app.route('/soccer')
def soccer() -> Any:
    """Recipes page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    documents = db_api.find_all({}, "soccer")

    context = {
        'title': 'Soccer',
        'recipes': documents['documents']
    }
    return render_template('soccer.html', **context)


@app.route('/f1')
def mma() -> Any:
    """Recipes page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    # documents = db_api.find_all({}, 'mma')

    # db_api.insert_one({"Testing": 4}, 'mma')


    conn = http.client.HTTPSConnection("v1.formula-1.api-sports.io")
    headers = {
		'x-rapidapi-host': "v1.formula-1.api-sports.io",
		'x-rapidapi-key': "293de58719e68eb4e6a3cd56865105e1"
    }
    payload = ''
    conn.request("GET", "/rankings/drivers?season=2023", payload, headers)
    res = conn.getresponse()
    data = res.read()

    j = data.decode("utf-8").replace("'", '"')
    dat = json.loads(j)

    season2023 = dat["response"]

    for driver in season2023:
        position = {
            "position": driver["position"],
            "driver": {
                "id": driver["driver"]["id"],
                "name": driver["driver"]["name"],
                "abbr": driver["driver"]["abbr"],
                "number": driver["driver"]["number"]
            },
            "team": {
                "id": driver["team"]["id"],
                "name": driver["driver"]["name"],
            },
            "points": driver["points"],
            "wins": driver["wins"],
            "behind": driver["behind"],
            "season": driver["season"]
        }

        insert_one(position, "mma")

        # print(position)


    
    context = {
        'title': 'Formula 1',
        # "content": res["documents"]
    }
    return render_template('f1.html', **context)


@app.route('/basketball')
def basketball() -> Any:
    """Recipes page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    documents = db_api.find_all({}, "basketball")

    context = {
        'title': 'Basketball',
        'recipes': documents['documents']
    }
    return render_template('basketball.html', **context)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5555))
    app.run(debug=True, host='0.0.0.0', port=port)
