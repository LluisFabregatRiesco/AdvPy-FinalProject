from flask import Flask, render_template
from pymongo.server_api import ServerApi
from pymongo import MongoClient

app = Flask(__name__)

path_to_certificate2 = 'lluis_cert.pem'
uri2 = "mongodb+srv://cluster0.0uqoz5p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client2 = MongoClient(uri2,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate2,
                     server_api=ServerApi('1'))
db2 = client2['sports']
collection2 = db2['soccer']  # MongoDB collection to store NBA standings


@app.route('/')
def index():
    # Retrieve standings data from MongoDB
    standings_data = collection.find_one()

    if standings_data:
        # Extract relevant information
        standings = standings_data.get("league", {}).get("standings", [])

        # Sort teams by ranking
        sorted_standings = sorted(standings[0], key=lambda x: x.get("rank", 0))

        return render_template('soccer.html', standings=sorted_standings)

    return "No data available."

if __name__ == '__main__':
    app.run(debug=True)
