"""
This is the main file of the Flask application.
"""

from typing import Any
import os
from flask import Flask, render_template

from pymongo.server_api import ServerApi
from pymongo import MongoClient

import db_api
# import http.client
# import json


app = Flask(__name__)

path_to_certificate = 'cert.pem'
uri = "mongodb+srv://cluster0.0uqoz5p."
uri += "mongodb.net/?authSource=%24external"
uri += "&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))
db = client['sports']
collection = db['basketball']  # MongoDB collection to store NBA standings


path_to_certificate2 = 'lluis_cert.pem'
uri2 = "mongodb+srv://cluster0.0uqoz5p."
uri2 += "mongodb.net/?authSource=%24external"
uri2 += "&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client2 = MongoClient(uri2,
                      tls=True,
                      tlsCertificateKeyFile=path_to_certificate2,
                      server_api=ServerApi('1'))
db2 = client2['sports']
collection2 = db2['soccer']  # MongoDB collection to store PL standings


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

    for i in range(2, 12):
        url = "/teams/statistics?league=1&season=2023&team="
        conn.request("GET", url+str(i), payload, headers)
        res = conn.getresponse()
        data = res.read()
        j = data.decode("utf-8").replace("'", '"')

        dat = json.loads(j)

        wins = dat["response"]["games"]["wins"]["all"]["total"]
        losses = dat["response"]["games"]["loses"]["all"]["total"]
        name = dat["response"]["team"]["name"]
        #print(dat["response"]["games"]["wins"]["all"]["total"])

        print("The "+name+" have won "+str(wins)+" and lost "+str(losses))

        db_api.insert_one({"Name": name, "Wins": wins, "Losses": losses})

        #db_api.insert_one({"Name": dat["response"][0]["name"],
        #"ID": dat["response"][0]["id"]})
    """

    res = db_api.find_all({})
    context = {
        "title": "Baseball",
        "content": res["documents"]
    }
    return render_template('baseball.html', **context)


@app.route('/soccer')
def soccer() -> Any:
    """Soccer page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    # Retrieve standings data from MongoDB
    standings_data = collection2.find_one()

    if standings_data:
        # Extract relevant information
        standings = standings_data.get("league", {}).get("standings", [])

        # Sort teams by ranking
        sorted_standings = sorted(standings[0], key=lambda x: x.get("rank", 0))

         # Extract additional information (record and goal difference)
        team_data_with_info = [
            {
                "rank": team.get("rank", ""),
                "name": team.get("team", {}).get("name", ""),
                "points": team.get("points", ""),
                "record": f"{team.get('all', {}).get('win', 0)}-{team.get('all', {}).get('draw', 0)}-{team.get('all', {}).get('lose', 0)}",
                "goal_difference": team.get("goalsDiff", "")
            }
            for team in sorted_standings
        ]

        return render_template('soccer.html', standings=sorted_standings)

    return "No data available."


@app.route('/mma')
def mma() -> Any:
    """MMA page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    documents = db_api.find_all({}, "mma")

    context = {
        'title': 'MMA',
        'recipes': documents['documents']
    }
    return render_template('mma.html', **context)


@app.route('/basketball')
def basketball() -> Any:
    """Basketball page of the application.

    Returns:
        str: HTML page using Jinja2 template.
    """
    # Fetch NBA standings data from MongoDB
    nba_standings = list(collection.find({}, {'_id': 0}).sort('rank'))

    return render_template('basketball.html', nba_standings=nba_standings)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5555))
    app.run(debug=True, host='0.0.0.0', port=port)
