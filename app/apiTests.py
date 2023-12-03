"""
This is the main file of the Flask application.
"""

# from typing import Any
from . import db_api


db_api.insert_one({"Testing", 4})
