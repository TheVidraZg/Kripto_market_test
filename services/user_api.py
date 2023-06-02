import requests

from models.user_model import User
from infrastructure.constants import REST_API_URL_BASE



root_url = REST_API_URL_BASE

def get_users_from_api():
    response = requests.get(f'{root_url}/users')
    return [User.from_dict(user_json) for user_json in response.json()]

def get_user_from_api(id: int):
    response = requests.get(f'{root_url}/users/{str(id)}')
    return User.from_dict(response.json())