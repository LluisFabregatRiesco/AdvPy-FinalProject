from pymongo import MongoClient
from pymongo.server_api import ServerApi
import requests
import json
import http.client

uri = "mongodb+srv://cluster0.0uqoz5p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

# Create a ServerApi instance
server_api = ServerApi('1')

# Pass the ServerApi instance to the MongoClient constructor
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='lluis_cert.pem',
                     server_api=server_api)

db = client['sports']
collection = db['soccer']
doc_count = collection.count_documents({})
print(doc_count)



# API request to get Premier League standings
conn = http.client.HTTPSConnection("v3.football.api-sports.io")
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "74cca3ec3a07675f82caaf8b138d7d2f"
}
conn.request("GET", "/standings?league=39&season=2019", headers=headers)
res = conn.getresponse()
data = res.read()

# Parse the API response
response_data = json.loads(data.decode("utf-8"))

# Extract relevant information
standings_info = response_data.get("response", [])

# Insert data into MongoDB
if standings_info:
    collection.insert_one(standings_info[0])

# Close the connection
conn.close()
client.close()


