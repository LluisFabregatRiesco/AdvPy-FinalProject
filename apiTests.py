import requests

url = "https://tank01-mlb-live-in-game-real-time-statistics.p.rapidapi.com"
#/getMLBTeams"


querystring = {"teamStats": "false", "topPerformers": "false"}

headers = {
    "X-RapidAPI-Key": """My API Key probably not important to hide
                         this but oh well""",
    "X-RapidAPI-Host": """tank01-mlb-live-in-game-real-time-statistics
                        .p.rapidapi.com"""
}

response = requests.get(url, headers=headers, params=querystring)

res = response.json()['body']

for i in range(0, len(res)):
    print(res[i]['teamCity'])
    print(res[i]['teamName'])
    print(res[i]['teamID'])
