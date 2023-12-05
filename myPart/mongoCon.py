from pymongo import MongoClient
from pymongo.server_api import ServerApi
import requests
import json
import http.client

# Your MongoDB connection setup
path_to_certificate = 'cert.pem'
uri = "mongodb+srv://cluster0.0uqoz5p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))
db = client['sports']
collection = db['basketball']  # MongoDB collection to store NBA standings

# Fetching NBA standings data from the sports API
conn = http.client.HTTPSConnection("v1.basketball.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.basketball.api-sports.io",
    'x-rapidapi-key': "98075f2b83333b68f2b8193d331e178e"
}

conn.request("GET", "/standings?league=12&season=2023-2024", headers=headers)

res = conn.getresponse()
data = res.read()

# Decode the response data
decoded_data = data.decode("utf-8")

# Parse the JSON response
json_data = json.loads(decoded_data)

# Check if 'response' exists and has data
if 'response' in json_data and json_data['response']:
    standings = json_data['response'][0]
    nba_standings = []

    for team_standings in standings:
        group_info = team_standings['group']
        if group_info['name'] in ['Eastern Conference', 'Western Conference']:
            team_doc = {
                "team_name": team_standings['team']['name'],
                "conference": group_info['name'],
                "rank": team_standings['position']
            }
            nba_standings.append(team_doc)

    if nba_standings:
        result = collection.insert_many(nba_standings)
        print("Inserted:", len(result.inserted_ids), "documents into the collection.")
    else:
        print("No standings data available for insertion.")

else:
    print("No standings data available.")
