"""
    MongoDB database APIs.
"""

import copy
from typing import Dict, List, Any
import requests
import settings


def create_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(settings.HEADERS)
    return session

def insert_one(data: Dict[str, Any]) -> 'requests.Response':

    session = create_session()
    action = f'{settings.END_POINT}/insertOne'
    print(action)
    payload: Dict[str, Any] = copy.deepcopy(settings.PAYLOAD)
    payload['document'] = data
    response = session.post(action, json=payload)
    return response

def find_all(query: Dict[str, Any]) -> Any:
    session = create_session()
    action = f'{settings.END_POINT}/find'
    payload: Dict[str, Any] = copy.deepcopy(settings.PAYLOAD)
    payload['filter'] = query
    response = session.post(action, json=payload)
    return response.json()