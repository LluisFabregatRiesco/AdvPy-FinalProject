"""
    MongoDB database APIs.
"""

import copy
from typing import Dict, Any
# from typing import List
import requests
import settings


def create_session() -> requests.Session:
    """Create a session with the API header.

    Returns:
        requests.Session: Session with the API header.
    """
    session = requests.Session()
    session.headers.update(settings.HEADERS)
    return session


def insert_one(data: Dict[str, Any]) -> 'requests.Response':
    """Insert data into the database.

    Args:
        data (Dict[str, Any]): Data to insert.

    Returns:
        requests.Response: Response from the API.
    """
    session = create_session()
    action = f'{settings.END_POINT}/insertOne'
    print(action)
    payload: Dict[str, Any] = copy.deepcopy(settings.PAYLOAD)
    payload['document'] = data
    response = session.post(action, json=payload)
    return response


def find_all(query: Dict[str, Any]) -> Any:
    """Find all data.

    Args:
        query (Dict[str, Any]): filter for find_all API.

    Returns:
        Any: Data.
    """
    session = create_session()
    action = f'{settings.END_POINT}/find'
    payload: Dict[str, Any] = copy.deepcopy(settings.PAYLOAD)
    payload['filter'] = query
    response = session.post(action, json=payload)
    return response.json()