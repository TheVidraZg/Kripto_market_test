from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user_model import User


db_engine = create_engine('sqlite:///db_data/py_crypto_app.db')
Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

# Sve funkcije koje pokrivaju CRUD operacije

def user_create(user: User):
    company = user.company


    entity = (session.query(User)
              .filter(User.name == user.name))
    
    if entity is None:
        entity = user
        session.add(entity)
        session.commit()


def user_get_all() -> list[User]:
    pass


def user_get(id: int) -> User:
    pass


def user_update(user: User):
    pass


def user_delete(id: int):
    pass