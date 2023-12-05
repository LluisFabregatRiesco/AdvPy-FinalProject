from flask import Flask, render_template
from pymongo.server_api import ServerApi
from pymongo import MongoClient

app = Flask(__name__)

path_to_certificate = 'cert.pem'
uri = "mongodb+srv://cluster0.0uqoz5p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))
db = client['sports']
collection = db['basketball']  # MongoDB collection to store NBA standings

@app.route('/')
def index():
    # Fetch NBA standings data from MongoDB
    nba_standings = list(collection.find({}, {'_id': 0}).sort('rank'))

    return render_template('index.html', nba_standings=nba_standings)

if __name__ == "__main__":
    app.run(debug=True)
