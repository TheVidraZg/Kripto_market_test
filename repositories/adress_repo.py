from models.adress_model import Address
from repositories.db_repo_init import session



def address_create(address: Address):
    entity = (session.query(Address)
              .filter(Address.city == address.city)
              .one_or_none())
    
    if entity is None:
        entity = address
        session.add(entity)
        session.commit()


def address_get_all() -> list[Address]:
    return (session.query(Address).all())


def address_get(id: int) -> Address:
    return (session.query(Address)
              .filter(Address.id == id)
              .one_or_none())


def address_update(address: Address):
    entity = (session.query(Address)
              .filter(Address.id == Address.id)
              .one_or_none())
    
    if entity is not None:
        entity = address
        session.commit()


def address_delete(id: int):
    entity = (session.query(Address)
              .filter(Address.id == id)
              .one_or_none())
    
    if entity is not None:
        session.delete(entity)
        session.commit()