"""
This is the main file of the Flask application.
"""

from typing import Any
import os
# import http.client
from flask import Flask, render_template
# from flask import request
# from . import forms
from . import db_api

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
    res = db_api.find_all({})
    context = {
        "title": "Baseball",
        "content": res["documents"]
    }
    return render_template('baseball.html', **context)


@app.route('/soccer')
def soccer() -> Any:
    # Retrieve standings data from MongoDB
    standings_data = collection.find_one()

    if standings_data:
        # Extract relevant information
        standings = standings_data.get("league", {}).get("standings", [])

        # Sort teams by ranking
        sorted_standings = sorted(standings[0], key=lambda x: x.get("rank", 0))

        return render_template('soccer.html', standings=sorted_standings)
    return "No data available."


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
