"""
Settings for the app.
"""

END_POINT = 'https://us-west-2.aws.data.mongodb-api.com/app/'
END_POINT += 'data-svyvw/endpoint/data/v1/action'
API_KEY = 'vV1IywCeTPSJSY5DBXTPLdhktuhTaXbPpNb0teFdHP2n4QzVPBn2CdCbGxXV5Kkc'
DATA_SOURCE = 'Cluster0'
DB_NAME = 'sports'
HEADERS = {'Content-Type': 'application/json',
           'Access-Control-Request-Headers': '*',
           'api-key': f'{API_KEY}'}

PAYLOAD = {
    "collection": None,
    "database": DB_NAME,
    "dataSource": DATA_SOURCE
}
