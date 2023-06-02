from sqlalchemy import create_engine

from models.user_model import Base
from services.user_api import get_users_from_api
from repositories.user_repo import user_create, db_engine




def db_init():
    Base.metadata.create_all(db_engine)


def db_seed():
    for user in get_users_from_api():
        user_create(user)