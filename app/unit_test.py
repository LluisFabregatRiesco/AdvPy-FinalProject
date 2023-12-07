from pymongo import MongoClient
from pymongo.server_api import ServerApi
from typing import Any
import unittest


class TestMongoDBConnection(unittest.TestCase):
    def test_mongodb_connection_carlos(self) -> Any:
        path_to_certificate = 'cert.pem'
        uri = "mongodb+srv://cluster0.0uqoz5p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority" # noqa E501

        try:
            client = MongoClient(uri,
                                 tls=True,
                                 tlsCertificateKeyFile=path_to_certificate,
                                 server_api=ServerApi('1'))
            db = client['sports']
            collection = db['basketball']

            # Check if the collection object exists
            self.assertIsNotNone(collection)
        except Exception as e:
            self.fail(f"Failed to establish MongoDB connection: {e}")

    def test_mongodb_connection_lluis(self) -> Any:
        path_to_certificate2 = 'lluis_cert.pem'
        uri2 = "mongodb+srv://cluster0.0uqoz5p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority" # noqa E501

        try:
            client2 = MongoClient(uri2,
                                  tls=True,
                                  tlsCertificateKeyFile=path_to_certificate2,
                                  server_api=ServerApi('1'))
            db2 = client2['sports']
            collection2 = db2['soccer']

            # Check if the collection2 object exists
            self.assertIsNotNone(collection2)
        except Exception as e:
            self.fail(f"Failed to establish second MongoDB connection: {e}")


if __name__ == '__main__':
    unittest.main()
