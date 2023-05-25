import requests

from models.user_model import User

root_url = 'https://jsonplaceholder.typicode.com'

def get_users_from_api():
    response = requests.get(f'{root_url}/users')

    # users_list = []
    # for user_json in response.json():
    #     users_list.append(User.from_dict(user_json))
    # return users_list

    return [User.from_dict(user_json) for user_json in response.json()]

def get_user_from_api(id: int):
    response = requests.get(f'{root_url}/users/{str(id)}')
    return User.from_dict(response.json())