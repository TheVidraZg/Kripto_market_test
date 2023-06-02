from sqlalchemy import and_

from models.user_model import User
from repositories.db_repo_init import session



def user_create(user: User):
    entity = (session.query(User)
              .filter(and_(
                    User.name == user.name,
                    User.username == user.username,
                    User.email == user.email
              ))
              .one_or_none())
    
    if entity is None:
        entity = user
        session.add(entity)
        session.commit()


def user_get_all() -> list[User]:
    return (session.query(User).all())


def user_get(id: int) -> User:
    return (session.query(User)
              .filter(User.id == id)
              .one_or_none())


def user_update(user: User):
    entity = (session.query(User)
              .filter(User.id == user.id)
              .one_or_none())
    
    if entity is not None:
        entity = user
        session.commit()


def user_delete(id: int):
    entity = (session.query(User)
              .filter(User.id == id)
              .one_or_none())
    
    if entity is not None:
        session.delete(entity)
        session.commit()